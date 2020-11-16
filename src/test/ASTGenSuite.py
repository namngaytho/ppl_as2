import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # def test_01(self):
    #     """Test simple VarDecl """
    #     input = """
    #         Var: x=3;
    #     """
    #     expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 1))

    # def test_02(self):
    #     """Test simple VarDecl """
    #     input = """ 
    #         Var: x=3,y,z=1.5e-1,t="abcd";
    #     """
    #     expect = Program([VarDecl(Id('x'), [], IntLiteral(3)), VarDecl((Id('y')), [],None), VarDecl(Id('z'), [], FloatLiteral(0.15)), VarDecl(Id('t'), [], StringLiteral('abcd'))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 2))

    # def test_03(self):
    #     """Test simple VarDecl """
    #     input = """
    #         Var: x[2][3][4]=True;
    #     """
    #     expect = Program([VarDecl(Id('x'),[IntLiteral(2),IntLiteral(3),IntLiteral(4)],BooleanLiteral('True'))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 3))
    
    # def test_04(self):
    #     """Test simple VarDecl """
    #     input = """
    #         Var: x={1,{"a"}};
    #     """
    #     expect = Program([VarDecl(Id('x'),[],ArrayLiteral([IntLiteral(1),ArrayLiteral([StringLiteral('a')])]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 4))

    # def test_05(self):
    #     """Test simple VarDecl """
    #     input = """
    #         Var : a=1e4,b=0.0e-5,c=0.00,d=0x322,e=0O12345;
    #     """
    #     expect = Program([VarDecl(Id('a'),[],FloatLiteral(10000.0)),VarDecl(Id('b'),[],FloatLiteral(0.0)),VarDecl(Id('c'),[],FloatLiteral(0.0)),VarDecl(Id('d'),[],IntLiteral(802)),VarDecl(Id('e'),[],IntLiteral(5349))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 5))

    # def test_06(self):
    #     """Test simple VarDecl """
    #     input = """
    #         Var: x;
    #         Var: y;
    #         Var: z;
    #         Var: t;
    #     """
    #     expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None),VarDecl(Id('t'),[],None)])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 6))  

    # def test_07(self):
    #     """Test simple FuncDecl """
    #     input = """
    #         Function: nam
    #         Body:
    #         EndBody.
    #     """
    #     expect = Program([FuncDecl(Id('nam'),[],([],[]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 7))

    # def test_08(self):
    #     """Test simple FuncDecl """
    #     input = """
    #         Function: nam
    #         Parameter: m,n
    #         Body:
    #         EndBody.
    #     """
    #     expect = Program([FuncDecl(Id('nam'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None)],([],[]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 8))

    # def test_09(self):
    #     """Test simple FuncDecl """
    #     input = """
    #         Function: nam
    #         Parameter: m,n
    #         Body:
    #         Var:hello=5;
    #         EndBody.
    #     """
    #     expect = Program([FuncDecl(Id('nam'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None)],([VarDecl(Id('hello'),[],IntLiteral(5))],[]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 9))

    # def test_10(self):
    #     """Test simple FuncDecl """
    #     input = """
    #         Function: nam
    #         Parameter: m,n
    #         Body:
    #         Var:hello=5;
    #         Return;
    #         EndBody.
    #     """
    #     expect = Program([FuncDecl(Id('nam'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None)],([VarDecl(Id('hello'),[],IntLiteral(5))],[Return(None)]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 10))
    
    # def test_11(self):
    #     """Test simple FuncDecl """
    #     input = """
    #         Function: a_Nam123456
    #         Parameter: m[2][3],n[6][9][8]
    #         Body:
    #         EndBody.
    #     """
    #     expect = Program([FuncDecl(Id('a_Nam123456'),[VarDecl(Id('m'),[IntLiteral(2),IntLiteral(3)],None),VarDecl(Id('n'),[IntLiteral(6),IntLiteral(9),IntLiteral(8)],None)],([],[]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 11))

    # def test_12(self):
    #     """Test simple FuncDecl """
    #     input = """
    #         Function: a_Nam123456
    #         Parameter: m[2][3],n[6][9][8]
    #         Body:
    #         Var: x=0xFF,y=0xFF,z=0o22;
    #         EndBody.
    #     """
    #     expect = Program([FuncDecl(Id('a_Nam123456'),[VarDecl(Id('m'),[IntLiteral(2),IntLiteral(3)],None),VarDecl(Id('n'),[IntLiteral(6),IntLiteral(9),IntLiteral(8)],None)],([VarDecl(Id('x'),[],IntLiteral(255)),VarDecl(Id('y'),[],IntLiteral(255)),VarDecl(Id('z'),[],IntLiteral(18))],[]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 12))
    
    # def test_13(self):
    #     """Test simple FuncDecl """
    #     input = """
    #         Function: thanhnam_1813130
    #         Parameter: m[2][3],n[6][9][8]
    #         Body:
    #         Var: x[1]={1,2,3};
    #         Var: y = "$%^%$^$";
    #         EndBody.
    #     """
    #     expect = Program([FuncDecl(Id('thanhnam_1813130'),[VarDecl(Id('m'),[IntLiteral(2),IntLiteral(3)],None),VarDecl(Id('n'),[IntLiteral(6),IntLiteral(9),IntLiteral(8)],None)],([VarDecl(Id('x'),[IntLiteral(1)],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id('y'),[],StringLiteral('$%^%$^$'))],[]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 13))
    
    # def test_14(self):
    #     """Test FuncDecl with assign_stm """
    #     input = """
    #         Function: nam
    #     Parameter: x,y,a[20]
    #     Body:
    #         y=x*2;
    #     EndBody.
    #     """
    #     expect = Program([FuncDecl(Id('nam')[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id(a),[IntLiteral(20)])],([][Assign(Id(y),BinaryOp(*,Id(x),IntLiteral(2)))]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 14))

    def test_15(self):
        """Test Complex FuncDecl """
        input = """
            Function: thanhnam_1813130
           
            Body:
            a = foo(2)[0xFF];
            foo(2); 
            foo(2)[3] = a+1; 
            a=foo(2);
            EndBody.
        """
        expect = Program([FuncDecl(Id('thanhnam_1813130'),[],([],[Assign(Id('a'),ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),[IntLiteral(255)])),CallStmt(Id('foo'),[IntLiteral(2)]),Assign(ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp('+',Id('a'),IntLiteral(1))),Assign(Id('a'),CallExpr(Id('foo'),[IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 15))

    def test_16(self):
        """Test Complex FuncDecl """
        input = """
            Function: sort
        Parameter: arr[0o100], left, right
        Body:
            For(i = left + 1, i <= right, 1) Do
                Var: temp, j;
                temp = arr[i];
                j = i - 1;
                While (j >= left) && (arr[j] > temp) Do
                    arr[j + 1] = arr[j];
                    j = j - 1;
                EndWhile.
                arr[j + 1] = temp;
            EndFor.
        EndBody.
            
        """
        expect =  Program([FuncDecl(Id('sort'), [VarDecl(Id('arr'), [0o100], None), VarDecl(Id('left'), [], None), VarDecl(Id('right'), [], None)], ([], [\
                For(Id('i'), BinaryOp('+', Id('left'), IntLiteral(1)), BinaryOp('<=', Id('i'), Id('right')), IntLiteral(1), ([VarDecl(Id('temp'), [], None), VarDecl(Id('j'), [], None)], \
                [Assign(Id('temp'), ArrayCell(Id('arr'), [Id('i')])), Assign(Id('j'), BinaryOp('-', Id('i'), IntLiteral(1))),\
                While(BinaryOp('&&', BinaryOp('>=', Id('j'), Id('left')), BinaryOp('>', ArrayCell(Id('arr'), [Id('j')]), Id('temp'))),([], [Assign(ArrayCell(Id('arr'), [BinaryOp('+', Id('j'), IntLiteral(1))]), ArrayCell(Id('arr'), [Id('j')])), Assign(Id('j'), BinaryOp('-', Id('j'), IntLiteral(1)))])),\
                Assign(ArrayCell(Id('arr'), [BinaryOp('+', Id('j'), IntLiteral(1))]), Id('temp'))
                ]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 16))

    def test_17(self):
        """Test Complex FuncDecl """
        input = """
            Function: main
        Body:
            a = f(2, 3 + 4)[10 * 0xFF];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [], ([], [Assign(Id('a'), ArrayCell(CallExpr(Id('f'), [IntLiteral(2), BinaryOp('+', IntLiteral(3), IntLiteral(4))]), [BinaryOp('*', IntLiteral(10), IntLiteral(255))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 17))

    def test_18(self):
        """Test Complex FuncDecl """
        input = """
            Function: main
        Body:
            **If statement**
            If a Then b();  Else EndIf.
        EndBody.
        """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 18))
    def test_19(self):
        """Test Complex FuncDecl """
        input = """
            Function: main
        Body:
            **If statement**
            If a Then  Else EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[If(Id(a),[],[])Else([],[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 19))