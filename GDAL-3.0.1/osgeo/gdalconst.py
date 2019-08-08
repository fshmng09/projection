# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gdalconst', [dirname(__file__)])
        except ImportError:
            import _gdalconst
            return _gdalconst
        if fp is not None:
            try:
                _mod = imp.load_module('_gdalconst', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gdalconst = swig_import_helper()
    del swig_import_helper
else:
    import _gdalconst
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_gdalconst.GDT_Unknown_swigconstant(_gdalconst)
GDT_Unknown = _gdalconst.GDT_Unknown

_gdalconst.GDT_Byte_swigconstant(_gdalconst)
GDT_Byte = _gdalconst.GDT_Byte

_gdalconst.GDT_UInt16_swigconstant(_gdalconst)
GDT_UInt16 = _gdalconst.GDT_UInt16

_gdalconst.GDT_Int16_swigconstant(_gdalconst)
GDT_Int16 = _gdalconst.GDT_Int16

_gdalconst.GDT_UInt32_swigconstant(_gdalconst)
GDT_UInt32 = _gdalconst.GDT_UInt32

_gdalconst.GDT_Int32_swigconstant(_gdalconst)
GDT_Int32 = _gdalconst.GDT_Int32

_gdalconst.GDT_Float32_swigconstant(_gdalconst)
GDT_Float32 = _gdalconst.GDT_Float32

_gdalconst.GDT_Float64_swigconstant(_gdalconst)
GDT_Float64 = _gdalconst.GDT_Float64

_gdalconst.GDT_CInt16_swigconstant(_gdalconst)
GDT_CInt16 = _gdalconst.GDT_CInt16

_gdalconst.GDT_CInt32_swigconstant(_gdalconst)
GDT_CInt32 = _gdalconst.GDT_CInt32

_gdalconst.GDT_CFloat32_swigconstant(_gdalconst)
GDT_CFloat32 = _gdalconst.GDT_CFloat32

_gdalconst.GDT_CFloat64_swigconstant(_gdalconst)
GDT_CFloat64 = _gdalconst.GDT_CFloat64

_gdalconst.GDT_TypeCount_swigconstant(_gdalconst)
GDT_TypeCount = _gdalconst.GDT_TypeCount

_gdalconst.GA_ReadOnly_swigconstant(_gdalconst)
GA_ReadOnly = _gdalconst.GA_ReadOnly

_gdalconst.GA_Update_swigconstant(_gdalconst)
GA_Update = _gdalconst.GA_Update

_gdalconst.GF_Read_swigconstant(_gdalconst)
GF_Read = _gdalconst.GF_Read

_gdalconst.GF_Write_swigconstant(_gdalconst)
GF_Write = _gdalconst.GF_Write

_gdalconst.GRIORA_NearestNeighbour_swigconstant(_gdalconst)
GRIORA_NearestNeighbour = _gdalconst.GRIORA_NearestNeighbour

_gdalconst.GRIORA_Bilinear_swigconstant(_gdalconst)
GRIORA_Bilinear = _gdalconst.GRIORA_Bilinear

_gdalconst.GRIORA_Cubic_swigconstant(_gdalconst)
GRIORA_Cubic = _gdalconst.GRIORA_Cubic

_gdalconst.GRIORA_CubicSpline_swigconstant(_gdalconst)
GRIORA_CubicSpline = _gdalconst.GRIORA_CubicSpline

_gdalconst.GRIORA_Lanczos_swigconstant(_gdalconst)
GRIORA_Lanczos = _gdalconst.GRIORA_Lanczos

_gdalconst.GRIORA_Average_swigconstant(_gdalconst)
GRIORA_Average = _gdalconst.GRIORA_Average

_gdalconst.GRIORA_Mode_swigconstant(_gdalconst)
GRIORA_Mode = _gdalconst.GRIORA_Mode

_gdalconst.GRIORA_Gauss_swigconstant(_gdalconst)
GRIORA_Gauss = _gdalconst.GRIORA_Gauss

_gdalconst.GCI_Undefined_swigconstant(_gdalconst)
GCI_Undefined = _gdalconst.GCI_Undefined

_gdalconst.GCI_GrayIndex_swigconstant(_gdalconst)
GCI_GrayIndex = _gdalconst.GCI_GrayIndex

_gdalconst.GCI_PaletteIndex_swigconstant(_gdalconst)
GCI_PaletteIndex = _gdalconst.GCI_PaletteIndex

_gdalconst.GCI_RedBand_swigconstant(_gdalconst)
GCI_RedBand = _gdalconst.GCI_RedBand

_gdalconst.GCI_GreenBand_swigconstant(_gdalconst)
GCI_GreenBand = _gdalconst.GCI_GreenBand

_gdalconst.GCI_BlueBand_swigconstant(_gdalconst)
GCI_BlueBand = _gdalconst.GCI_BlueBand

_gdalconst.GCI_AlphaBand_swigconstant(_gdalconst)
GCI_AlphaBand = _gdalconst.GCI_AlphaBand

_gdalconst.GCI_HueBand_swigconstant(_gdalconst)
GCI_HueBand = _gdalconst.GCI_HueBand

_gdalconst.GCI_SaturationBand_swigconstant(_gdalconst)
GCI_SaturationBand = _gdalconst.GCI_SaturationBand

_gdalconst.GCI_LightnessBand_swigconstant(_gdalconst)
GCI_LightnessBand = _gdalconst.GCI_LightnessBand

_gdalconst.GCI_CyanBand_swigconstant(_gdalconst)
GCI_CyanBand = _gdalconst.GCI_CyanBand

_gdalconst.GCI_MagentaBand_swigconstant(_gdalconst)
GCI_MagentaBand = _gdalconst.GCI_MagentaBand

_gdalconst.GCI_YellowBand_swigconstant(_gdalconst)
GCI_YellowBand = _gdalconst.GCI_YellowBand

_gdalconst.GCI_BlackBand_swigconstant(_gdalconst)
GCI_BlackBand = _gdalconst.GCI_BlackBand

_gdalconst.GCI_YCbCr_YBand_swigconstant(_gdalconst)
GCI_YCbCr_YBand = _gdalconst.GCI_YCbCr_YBand

_gdalconst.GCI_YCbCr_CrBand_swigconstant(_gdalconst)
GCI_YCbCr_CrBand = _gdalconst.GCI_YCbCr_CrBand

_gdalconst.GCI_YCbCr_CbBand_swigconstant(_gdalconst)
GCI_YCbCr_CbBand = _gdalconst.GCI_YCbCr_CbBand

_gdalconst.GRA_NearestNeighbour_swigconstant(_gdalconst)
GRA_NearestNeighbour = _gdalconst.GRA_NearestNeighbour

_gdalconst.GRA_Bilinear_swigconstant(_gdalconst)
GRA_Bilinear = _gdalconst.GRA_Bilinear

_gdalconst.GRA_Cubic_swigconstant(_gdalconst)
GRA_Cubic = _gdalconst.GRA_Cubic

_gdalconst.GRA_CubicSpline_swigconstant(_gdalconst)
GRA_CubicSpline = _gdalconst.GRA_CubicSpline

_gdalconst.GRA_Lanczos_swigconstant(_gdalconst)
GRA_Lanczos = _gdalconst.GRA_Lanczos

_gdalconst.GRA_Average_swigconstant(_gdalconst)
GRA_Average = _gdalconst.GRA_Average

_gdalconst.GRA_Mode_swigconstant(_gdalconst)
GRA_Mode = _gdalconst.GRA_Mode

_gdalconst.GRA_Max_swigconstant(_gdalconst)
GRA_Max = _gdalconst.GRA_Max

_gdalconst.GRA_Min_swigconstant(_gdalconst)
GRA_Min = _gdalconst.GRA_Min

_gdalconst.GRA_Med_swigconstant(_gdalconst)
GRA_Med = _gdalconst.GRA_Med

_gdalconst.GRA_Q1_swigconstant(_gdalconst)
GRA_Q1 = _gdalconst.GRA_Q1

_gdalconst.GRA_Q3_swigconstant(_gdalconst)
GRA_Q3 = _gdalconst.GRA_Q3

_gdalconst.GPI_Gray_swigconstant(_gdalconst)
GPI_Gray = _gdalconst.GPI_Gray

_gdalconst.GPI_RGB_swigconstant(_gdalconst)
GPI_RGB = _gdalconst.GPI_RGB

_gdalconst.GPI_CMYK_swigconstant(_gdalconst)
GPI_CMYK = _gdalconst.GPI_CMYK

_gdalconst.GPI_HLS_swigconstant(_gdalconst)
GPI_HLS = _gdalconst.GPI_HLS

_gdalconst.CXT_Element_swigconstant(_gdalconst)
CXT_Element = _gdalconst.CXT_Element

_gdalconst.CXT_Text_swigconstant(_gdalconst)
CXT_Text = _gdalconst.CXT_Text

_gdalconst.CXT_Attribute_swigconstant(_gdalconst)
CXT_Attribute = _gdalconst.CXT_Attribute

_gdalconst.CXT_Comment_swigconstant(_gdalconst)
CXT_Comment = _gdalconst.CXT_Comment

_gdalconst.CXT_Literal_swigconstant(_gdalconst)
CXT_Literal = _gdalconst.CXT_Literal

_gdalconst.CE_None_swigconstant(_gdalconst)
CE_None = _gdalconst.CE_None

_gdalconst.CE_Debug_swigconstant(_gdalconst)
CE_Debug = _gdalconst.CE_Debug

_gdalconst.CE_Warning_swigconstant(_gdalconst)
CE_Warning = _gdalconst.CE_Warning

_gdalconst.CE_Failure_swigconstant(_gdalconst)
CE_Failure = _gdalconst.CE_Failure

_gdalconst.CE_Fatal_swigconstant(_gdalconst)
CE_Fatal = _gdalconst.CE_Fatal

_gdalconst.CPLE_None_swigconstant(_gdalconst)
CPLE_None = _gdalconst.CPLE_None

_gdalconst.CPLE_AppDefined_swigconstant(_gdalconst)
CPLE_AppDefined = _gdalconst.CPLE_AppDefined

_gdalconst.CPLE_OutOfMemory_swigconstant(_gdalconst)
CPLE_OutOfMemory = _gdalconst.CPLE_OutOfMemory

_gdalconst.CPLE_FileIO_swigconstant(_gdalconst)
CPLE_FileIO = _gdalconst.CPLE_FileIO

_gdalconst.CPLE_OpenFailed_swigconstant(_gdalconst)
CPLE_OpenFailed = _gdalconst.CPLE_OpenFailed

_gdalconst.CPLE_IllegalArg_swigconstant(_gdalconst)
CPLE_IllegalArg = _gdalconst.CPLE_IllegalArg

_gdalconst.CPLE_NotSupported_swigconstant(_gdalconst)
CPLE_NotSupported = _gdalconst.CPLE_NotSupported

_gdalconst.CPLE_AssertionFailed_swigconstant(_gdalconst)
CPLE_AssertionFailed = _gdalconst.CPLE_AssertionFailed

_gdalconst.CPLE_NoWriteAccess_swigconstant(_gdalconst)
CPLE_NoWriteAccess = _gdalconst.CPLE_NoWriteAccess

_gdalconst.CPLE_UserInterrupt_swigconstant(_gdalconst)
CPLE_UserInterrupt = _gdalconst.CPLE_UserInterrupt

_gdalconst.CPLE_ObjectNull_swigconstant(_gdalconst)
CPLE_ObjectNull = _gdalconst.CPLE_ObjectNull

_gdalconst.CPLE_HttpResponse_swigconstant(_gdalconst)
CPLE_HttpResponse = _gdalconst.CPLE_HttpResponse

_gdalconst.CPLE_AWSBucketNotFound_swigconstant(_gdalconst)
CPLE_AWSBucketNotFound = _gdalconst.CPLE_AWSBucketNotFound

_gdalconst.CPLE_AWSObjectNotFound_swigconstant(_gdalconst)
CPLE_AWSObjectNotFound = _gdalconst.CPLE_AWSObjectNotFound

_gdalconst.CPLE_AWSAccessDenied_swigconstant(_gdalconst)
CPLE_AWSAccessDenied = _gdalconst.CPLE_AWSAccessDenied

_gdalconst.CPLE_AWSInvalidCredentials_swigconstant(_gdalconst)
CPLE_AWSInvalidCredentials = _gdalconst.CPLE_AWSInvalidCredentials

_gdalconst.CPLE_AWSSignatureDoesNotMatch_swigconstant(_gdalconst)
CPLE_AWSSignatureDoesNotMatch = _gdalconst.CPLE_AWSSignatureDoesNotMatch

_gdalconst.OF_ALL_swigconstant(_gdalconst)
OF_ALL = _gdalconst.OF_ALL

_gdalconst.OF_RASTER_swigconstant(_gdalconst)
OF_RASTER = _gdalconst.OF_RASTER

_gdalconst.OF_VECTOR_swigconstant(_gdalconst)
OF_VECTOR = _gdalconst.OF_VECTOR

_gdalconst.OF_GNM_swigconstant(_gdalconst)
OF_GNM = _gdalconst.OF_GNM

_gdalconst.OF_READONLY_swigconstant(_gdalconst)
OF_READONLY = _gdalconst.OF_READONLY

_gdalconst.OF_UPDATE_swigconstant(_gdalconst)
OF_UPDATE = _gdalconst.OF_UPDATE

_gdalconst.OF_SHARED_swigconstant(_gdalconst)
OF_SHARED = _gdalconst.OF_SHARED

_gdalconst.OF_VERBOSE_ERROR_swigconstant(_gdalconst)
OF_VERBOSE_ERROR = _gdalconst.OF_VERBOSE_ERROR

_gdalconst.DMD_LONGNAME_swigconstant(_gdalconst)
DMD_LONGNAME = _gdalconst.DMD_LONGNAME

_gdalconst.DMD_HELPTOPIC_swigconstant(_gdalconst)
DMD_HELPTOPIC = _gdalconst.DMD_HELPTOPIC

_gdalconst.DMD_MIMETYPE_swigconstant(_gdalconst)
DMD_MIMETYPE = _gdalconst.DMD_MIMETYPE

_gdalconst.DMD_EXTENSION_swigconstant(_gdalconst)
DMD_EXTENSION = _gdalconst.DMD_EXTENSION

_gdalconst.DMD_EXTENSIONS_swigconstant(_gdalconst)
DMD_EXTENSIONS = _gdalconst.DMD_EXTENSIONS

_gdalconst.DMD_CONNECTION_PREFIX_swigconstant(_gdalconst)
DMD_CONNECTION_PREFIX = _gdalconst.DMD_CONNECTION_PREFIX

_gdalconst.DMD_CREATIONOPTIONLIST_swigconstant(_gdalconst)
DMD_CREATIONOPTIONLIST = _gdalconst.DMD_CREATIONOPTIONLIST

_gdalconst.DMD_CREATIONDATATYPES_swigconstant(_gdalconst)
DMD_CREATIONDATATYPES = _gdalconst.DMD_CREATIONDATATYPES

_gdalconst.DMD_CREATIONFIELDDATATYPES_swigconstant(_gdalconst)
DMD_CREATIONFIELDDATATYPES = _gdalconst.DMD_CREATIONFIELDDATATYPES

_gdalconst.DMD_SUBDATASETS_swigconstant(_gdalconst)
DMD_SUBDATASETS = _gdalconst.DMD_SUBDATASETS

_gdalconst.DCAP_OPEN_swigconstant(_gdalconst)
DCAP_OPEN = _gdalconst.DCAP_OPEN

_gdalconst.DCAP_CREATE_swigconstant(_gdalconst)
DCAP_CREATE = _gdalconst.DCAP_CREATE

_gdalconst.DCAP_CREATECOPY_swigconstant(_gdalconst)
DCAP_CREATECOPY = _gdalconst.DCAP_CREATECOPY

_gdalconst.DCAP_VIRTUALIO_swigconstant(_gdalconst)
DCAP_VIRTUALIO = _gdalconst.DCAP_VIRTUALIO

_gdalconst.DCAP_RASTER_swigconstant(_gdalconst)
DCAP_RASTER = _gdalconst.DCAP_RASTER

_gdalconst.DCAP_VECTOR_swigconstant(_gdalconst)
DCAP_VECTOR = _gdalconst.DCAP_VECTOR

_gdalconst.DCAP_NOTNULL_FIELDS_swigconstant(_gdalconst)
DCAP_NOTNULL_FIELDS = _gdalconst.DCAP_NOTNULL_FIELDS

_gdalconst.DCAP_DEFAULT_FIELDS_swigconstant(_gdalconst)
DCAP_DEFAULT_FIELDS = _gdalconst.DCAP_DEFAULT_FIELDS

_gdalconst.DCAP_NOTNULL_GEOMFIELDS_swigconstant(_gdalconst)
DCAP_NOTNULL_GEOMFIELDS = _gdalconst.DCAP_NOTNULL_GEOMFIELDS

_gdalconst.CPLES_BackslashQuotable_swigconstant(_gdalconst)
CPLES_BackslashQuotable = _gdalconst.CPLES_BackslashQuotable

_gdalconst.CPLES_XML_swigconstant(_gdalconst)
CPLES_XML = _gdalconst.CPLES_XML

_gdalconst.CPLES_URL_swigconstant(_gdalconst)
CPLES_URL = _gdalconst.CPLES_URL

_gdalconst.CPLES_SQL_swigconstant(_gdalconst)
CPLES_SQL = _gdalconst.CPLES_SQL

_gdalconst.CPLES_CSV_swigconstant(_gdalconst)
CPLES_CSV = _gdalconst.CPLES_CSV

_gdalconst.GFT_Integer_swigconstant(_gdalconst)
GFT_Integer = _gdalconst.GFT_Integer

_gdalconst.GFT_Real_swigconstant(_gdalconst)
GFT_Real = _gdalconst.GFT_Real

_gdalconst.GFT_String_swigconstant(_gdalconst)
GFT_String = _gdalconst.GFT_String

_gdalconst.GFU_Generic_swigconstant(_gdalconst)
GFU_Generic = _gdalconst.GFU_Generic

_gdalconst.GFU_PixelCount_swigconstant(_gdalconst)
GFU_PixelCount = _gdalconst.GFU_PixelCount

_gdalconst.GFU_Name_swigconstant(_gdalconst)
GFU_Name = _gdalconst.GFU_Name

_gdalconst.GFU_Min_swigconstant(_gdalconst)
GFU_Min = _gdalconst.GFU_Min

_gdalconst.GFU_Max_swigconstant(_gdalconst)
GFU_Max = _gdalconst.GFU_Max

_gdalconst.GFU_MinMax_swigconstant(_gdalconst)
GFU_MinMax = _gdalconst.GFU_MinMax

_gdalconst.GFU_Red_swigconstant(_gdalconst)
GFU_Red = _gdalconst.GFU_Red

_gdalconst.GFU_Green_swigconstant(_gdalconst)
GFU_Green = _gdalconst.GFU_Green

_gdalconst.GFU_Blue_swigconstant(_gdalconst)
GFU_Blue = _gdalconst.GFU_Blue

_gdalconst.GFU_Alpha_swigconstant(_gdalconst)
GFU_Alpha = _gdalconst.GFU_Alpha

_gdalconst.GFU_RedMin_swigconstant(_gdalconst)
GFU_RedMin = _gdalconst.GFU_RedMin

_gdalconst.GFU_GreenMin_swigconstant(_gdalconst)
GFU_GreenMin = _gdalconst.GFU_GreenMin

_gdalconst.GFU_BlueMin_swigconstant(_gdalconst)
GFU_BlueMin = _gdalconst.GFU_BlueMin

_gdalconst.GFU_AlphaMin_swigconstant(_gdalconst)
GFU_AlphaMin = _gdalconst.GFU_AlphaMin

_gdalconst.GFU_RedMax_swigconstant(_gdalconst)
GFU_RedMax = _gdalconst.GFU_RedMax

_gdalconst.GFU_GreenMax_swigconstant(_gdalconst)
GFU_GreenMax = _gdalconst.GFU_GreenMax

_gdalconst.GFU_BlueMax_swigconstant(_gdalconst)
GFU_BlueMax = _gdalconst.GFU_BlueMax

_gdalconst.GFU_AlphaMax_swigconstant(_gdalconst)
GFU_AlphaMax = _gdalconst.GFU_AlphaMax

_gdalconst.GFU_MaxCount_swigconstant(_gdalconst)
GFU_MaxCount = _gdalconst.GFU_MaxCount

_gdalconst.GRTT_THEMATIC_swigconstant(_gdalconst)
GRTT_THEMATIC = _gdalconst.GRTT_THEMATIC

_gdalconst.GRTT_ATHEMATIC_swigconstant(_gdalconst)
GRTT_ATHEMATIC = _gdalconst.GRTT_ATHEMATIC

_gdalconst.GMF_ALL_VALID_swigconstant(_gdalconst)
GMF_ALL_VALID = _gdalconst.GMF_ALL_VALID

_gdalconst.GMF_PER_DATASET_swigconstant(_gdalconst)
GMF_PER_DATASET = _gdalconst.GMF_PER_DATASET

_gdalconst.GMF_ALPHA_swigconstant(_gdalconst)
GMF_ALPHA = _gdalconst.GMF_ALPHA

_gdalconst.GMF_NODATA_swigconstant(_gdalconst)
GMF_NODATA = _gdalconst.GMF_NODATA

_gdalconst.GDAL_DATA_COVERAGE_STATUS_UNIMPLEMENTED_swigconstant(_gdalconst)
GDAL_DATA_COVERAGE_STATUS_UNIMPLEMENTED = _gdalconst.GDAL_DATA_COVERAGE_STATUS_UNIMPLEMENTED

_gdalconst.GDAL_DATA_COVERAGE_STATUS_DATA_swigconstant(_gdalconst)
GDAL_DATA_COVERAGE_STATUS_DATA = _gdalconst.GDAL_DATA_COVERAGE_STATUS_DATA

_gdalconst.GDAL_DATA_COVERAGE_STATUS_EMPTY_swigconstant(_gdalconst)
GDAL_DATA_COVERAGE_STATUS_EMPTY = _gdalconst.GDAL_DATA_COVERAGE_STATUS_EMPTY

_gdalconst.GARIO_PENDING_swigconstant(_gdalconst)
GARIO_PENDING = _gdalconst.GARIO_PENDING

_gdalconst.GARIO_UPDATE_swigconstant(_gdalconst)
GARIO_UPDATE = _gdalconst.GARIO_UPDATE

_gdalconst.GARIO_ERROR_swigconstant(_gdalconst)
GARIO_ERROR = _gdalconst.GARIO_ERROR

_gdalconst.GARIO_COMPLETE_swigconstant(_gdalconst)
GARIO_COMPLETE = _gdalconst.GARIO_COMPLETE

_gdalconst.GTO_TIP_swigconstant(_gdalconst)
GTO_TIP = _gdalconst.GTO_TIP

_gdalconst.GTO_BIT_swigconstant(_gdalconst)
GTO_BIT = _gdalconst.GTO_BIT

_gdalconst.GTO_BSQ_swigconstant(_gdalconst)
GTO_BSQ = _gdalconst.GTO_BSQ
# This file is compatible with both classic and new-style classes.


