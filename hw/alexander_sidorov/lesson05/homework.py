from ast import Assign
from ast import Attribute
from ast import Call
from ast import Compare
from ast import Constant
from ast import Expr
from ast import FunctionDef
from ast import List
from ast import Load
from ast import Module
from ast import Name
from ast import NotIn
from ast import Return
from ast import Store
from ast import Subscript
from ast import UnaryOp
from ast import USub
from ast import While
from ast import arg
from ast import arguments
from ast import fix_missing_locations
from string import ascii_letters
from typing import Any
from typing import Callable
from typing import Dict

tree = Module(
    body=[
        FunctionDef(
            name="hack",
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg="cipher", annotation=Name(id="str", ctx=Load())),
                    arg(arg="key", annotation=Name(id="str", ctx=Load())),
                ],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id="translation", ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id="str", ctx=Load()),
                            attr="maketrans",
                            ctx=Load(),
                        ),
                        args=[
                            Name(id="ascii_letters", ctx=Load()),
                            Name(id="key", ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id="responses", ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                ),
                Assign(
                    targets=[Name(id="response", ctx=Store())],
                    value=Name(id="cipher", ctx=Load()),
                ),
                While(
                    test=Compare(
                        left=Name(id="response", ctx=Load()),
                        ops=[NotIn()],
                        comparators=[Name(id="responses", ctx=Load())],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="responses", ctx=Load()),
                                    attr="append",
                                    ctx=Load(),
                                ),
                                args=[Name(id="response", ctx=Load())],
                                keywords=[],
                            )
                        ),
                        Assign(
                            targets=[Name(id="response", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="response", ctx=Load()),
                                    attr="translate",
                                    ctx=Load(),
                                ),
                                args=[Name(id="translation", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Subscript(
                        value=Name(id="responses", ctx=Load()),
                        slice=UnaryOp(op=USub(), operand=Constant(value=1)),
                        ctx=Load(),
                    )
                ),
            ],
            decorator_list=[],
            returns=Name(id="str", ctx=Load()),
        )
    ],
    type_ignores=[],
)

fix_missing_locations(tree)

namespace: Dict[str, Any] = {"ascii_letters": ascii_letters}

bytecode = compile(tree, filename=__name__, mode="exec")  # noqa: DUO110

exec(bytecode, namespace)  # noqa: DUO105,S102

hack: Callable = namespace["hack"]

assert callable(hack)
