from ctypes import c_uint
from ctypes import POINTER, c_char_p, c_int

from . import ffi

ffi.lib.lld_main_2.restype = c_int
ffi.lib.lld_main_2.argtypes = [c_char_p, c_char_p]
def lld_main_help():
    """
    Shows help for lld.
    """
    r = ffi.lib.lld_main_2(c_char_p("ld.lld".encode()),
        c_char_p("--help".encode()))
    if r != 0:
        raise Exception("lld_main() failed, error code: %d" % r)


def initialize():
    """
    Initialize the LLVM core.
    """
    ffi.lib.LLVMPY_InitializeCore()


def initialize_all_targets():
    """
    Initialize all targets. Necessary before targets can be looked up
    via the :class:`Target` class.
    """
    ffi.lib.LLVMPY_InitializeAllTargetInfos()
    ffi.lib.LLVMPY_InitializeAllTargets()
    ffi.lib.LLVMPY_InitializeAllTargetMCs()

def initialize_all_asmprinters():
    """
    Initialize all code generators. Necessary before generating
    any assembly or machine code via the :meth:`TargetMachine.emit_object`
    and :meth:`TargetMachine.emit_assembly` methods.
    """
    ffi.lib.LLVMPY_InitializeAllAsmPrinters()


def initialize_native_target():
    """
    Initialize the native (host) target.  Necessary before doing any
    code generation.
    """
    ffi.lib.LLVMPY_InitializeNativeTarget()


def initialize_native_asmprinter():
    """
    Initialize the native ASM printer.
    """
    ffi.lib.LLVMPY_InitializeNativeAsmPrinter()


def initialize_native_asmparser():
    """
    Initialize the native ASM parser.
    """
    ffi.lib.LLVMPY_InitializeNativeAsmParser()


def shutdown():
    ffi.lib.LLVMPY_Shutdown()


# =============================================================================
# Set function FFI

ffi.lib.LLVMPY_GetVersionInfo.restype = c_uint


def _version_info():
    v = []
    x = ffi.lib.LLVMPY_GetVersionInfo()
    while x:
        v.append(x & 0xff)
        x >>= 8
    return tuple(reversed(v))

llvm_version_info = _version_info()
