# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _gdalconst
else:
    import _gdalconst

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


GDT_Unknown = _gdalconst.GDT_Unknown
GDT_Byte = _gdalconst.GDT_Byte
GDT_UInt16 = _gdalconst.GDT_UInt16
GDT_Int16 = _gdalconst.GDT_Int16
GDT_UInt32 = _gdalconst.GDT_UInt32
GDT_Int32 = _gdalconst.GDT_Int32
GDT_UInt64 = _gdalconst.GDT_UInt64
GDT_Int64 = _gdalconst.GDT_Int64
GDT_Float32 = _gdalconst.GDT_Float32
GDT_Float64 = _gdalconst.GDT_Float64
GDT_CInt16 = _gdalconst.GDT_CInt16
GDT_CInt32 = _gdalconst.GDT_CInt32
GDT_CFloat32 = _gdalconst.GDT_CFloat32
GDT_CFloat64 = _gdalconst.GDT_CFloat64
GDT_TypeCount = _gdalconst.GDT_TypeCount
GA_ReadOnly = _gdalconst.GA_ReadOnly
GA_Update = _gdalconst.GA_Update
GF_Read = _gdalconst.GF_Read
GF_Write = _gdalconst.GF_Write
GRIORA_NearestNeighbour = _gdalconst.GRIORA_NearestNeighbour
GRIORA_Bilinear = _gdalconst.GRIORA_Bilinear
GRIORA_Cubic = _gdalconst.GRIORA_Cubic
GRIORA_CubicSpline = _gdalconst.GRIORA_CubicSpline
GRIORA_Lanczos = _gdalconst.GRIORA_Lanczos
GRIORA_Average = _gdalconst.GRIORA_Average
GRIORA_RMS = _gdalconst.GRIORA_RMS
GRIORA_Mode = _gdalconst.GRIORA_Mode
GRIORA_Gauss = _gdalconst.GRIORA_Gauss
GCI_Undefined = _gdalconst.GCI_Undefined
GCI_GrayIndex = _gdalconst.GCI_GrayIndex
GCI_PaletteIndex = _gdalconst.GCI_PaletteIndex
GCI_RedBand = _gdalconst.GCI_RedBand
GCI_GreenBand = _gdalconst.GCI_GreenBand
GCI_BlueBand = _gdalconst.GCI_BlueBand
GCI_AlphaBand = _gdalconst.GCI_AlphaBand
GCI_HueBand = _gdalconst.GCI_HueBand
GCI_SaturationBand = _gdalconst.GCI_SaturationBand
GCI_LightnessBand = _gdalconst.GCI_LightnessBand
GCI_CyanBand = _gdalconst.GCI_CyanBand
GCI_MagentaBand = _gdalconst.GCI_MagentaBand
GCI_YellowBand = _gdalconst.GCI_YellowBand
GCI_BlackBand = _gdalconst.GCI_BlackBand
GCI_YCbCr_YBand = _gdalconst.GCI_YCbCr_YBand
GCI_YCbCr_CrBand = _gdalconst.GCI_YCbCr_CrBand
GCI_YCbCr_CbBand = _gdalconst.GCI_YCbCr_CbBand
GRA_NearestNeighbour = _gdalconst.GRA_NearestNeighbour
GRA_Bilinear = _gdalconst.GRA_Bilinear
GRA_Cubic = _gdalconst.GRA_Cubic
GRA_CubicSpline = _gdalconst.GRA_CubicSpline
GRA_Lanczos = _gdalconst.GRA_Lanczos
GRA_Average = _gdalconst.GRA_Average
GRA_RMS = _gdalconst.GRA_RMS
GRA_Mode = _gdalconst.GRA_Mode
GRA_Max = _gdalconst.GRA_Max
GRA_Min = _gdalconst.GRA_Min
GRA_Med = _gdalconst.GRA_Med
GRA_Q1 = _gdalconst.GRA_Q1
GRA_Q3 = _gdalconst.GRA_Q3
GRA_Sum = _gdalconst.GRA_Sum
GPI_Gray = _gdalconst.GPI_Gray
GPI_RGB = _gdalconst.GPI_RGB
GPI_CMYK = _gdalconst.GPI_CMYK
GPI_HLS = _gdalconst.GPI_HLS
CXT_Element = _gdalconst.CXT_Element
CXT_Text = _gdalconst.CXT_Text
CXT_Attribute = _gdalconst.CXT_Attribute
CXT_Comment = _gdalconst.CXT_Comment
CXT_Literal = _gdalconst.CXT_Literal
CE_None = _gdalconst.CE_None
CE_Debug = _gdalconst.CE_Debug
CE_Warning = _gdalconst.CE_Warning
CE_Failure = _gdalconst.CE_Failure
CE_Fatal = _gdalconst.CE_Fatal
CPLE_None = _gdalconst.CPLE_None
CPLE_AppDefined = _gdalconst.CPLE_AppDefined
CPLE_OutOfMemory = _gdalconst.CPLE_OutOfMemory
CPLE_FileIO = _gdalconst.CPLE_FileIO
CPLE_OpenFailed = _gdalconst.CPLE_OpenFailed
CPLE_IllegalArg = _gdalconst.CPLE_IllegalArg
CPLE_NotSupported = _gdalconst.CPLE_NotSupported
CPLE_AssertionFailed = _gdalconst.CPLE_AssertionFailed
CPLE_NoWriteAccess = _gdalconst.CPLE_NoWriteAccess
CPLE_UserInterrupt = _gdalconst.CPLE_UserInterrupt
CPLE_ObjectNull = _gdalconst.CPLE_ObjectNull
CPLE_HttpResponse = _gdalconst.CPLE_HttpResponse
CPLE_AWSBucketNotFound = _gdalconst.CPLE_AWSBucketNotFound
CPLE_AWSObjectNotFound = _gdalconst.CPLE_AWSObjectNotFound
CPLE_AWSAccessDenied = _gdalconst.CPLE_AWSAccessDenied
CPLE_AWSInvalidCredentials = _gdalconst.CPLE_AWSInvalidCredentials
CPLE_AWSSignatureDoesNotMatch = _gdalconst.CPLE_AWSSignatureDoesNotMatch
OF_ALL = _gdalconst.OF_ALL
OF_RASTER = _gdalconst.OF_RASTER
OF_VECTOR = _gdalconst.OF_VECTOR
OF_GNM = _gdalconst.OF_GNM
OF_MULTIDIM_RASTER = _gdalconst.OF_MULTIDIM_RASTER
OF_READONLY = _gdalconst.OF_READONLY
OF_UPDATE = _gdalconst.OF_UPDATE
OF_SHARED = _gdalconst.OF_SHARED
OF_VERBOSE_ERROR = _gdalconst.OF_VERBOSE_ERROR
DMD_LONGNAME = _gdalconst.DMD_LONGNAME
DMD_HELPTOPIC = _gdalconst.DMD_HELPTOPIC
DMD_MIMETYPE = _gdalconst.DMD_MIMETYPE
DMD_EXTENSION = _gdalconst.DMD_EXTENSION
DMD_CONNECTION_PREFIX = _gdalconst.DMD_CONNECTION_PREFIX
DMD_EXTENSIONS = _gdalconst.DMD_EXTENSIONS
DMD_CREATIONOPTIONLIST = _gdalconst.DMD_CREATIONOPTIONLIST
DMD_MULTIDIM_DATASET_CREATIONOPTIONLIST = _gdalconst.DMD_MULTIDIM_DATASET_CREATIONOPTIONLIST
DMD_MULTIDIM_GROUP_CREATIONOPTIONLIST = _gdalconst.DMD_MULTIDIM_GROUP_CREATIONOPTIONLIST
DMD_MULTIDIM_DIMENSION_CREATIONOPTIONLIST = _gdalconst.DMD_MULTIDIM_DIMENSION_CREATIONOPTIONLIST
DMD_MULTIDIM_ARRAY_CREATIONOPTIONLIST = _gdalconst.DMD_MULTIDIM_ARRAY_CREATIONOPTIONLIST
DMD_MULTIDIM_ATTRIBUTE_CREATIONOPTIONLIST = _gdalconst.DMD_MULTIDIM_ATTRIBUTE_CREATIONOPTIONLIST
DMD_OPENOPTIONLIST = _gdalconst.DMD_OPENOPTIONLIST
DMD_CREATIONDATATYPES = _gdalconst.DMD_CREATIONDATATYPES
DMD_CREATIONFIELDDATATYPES = _gdalconst.DMD_CREATIONFIELDDATATYPES
DMD_CREATIONFIELDDATASUBTYPES = _gdalconst.DMD_CREATIONFIELDDATASUBTYPES
DMD_SUBDATASETS = _gdalconst.DMD_SUBDATASETS
DMD_CREATION_FIELD_DOMAIN_TYPES = _gdalconst.DMD_CREATION_FIELD_DOMAIN_TYPES
DCAP_OPEN = _gdalconst.DCAP_OPEN
DCAP_CREATE = _gdalconst.DCAP_CREATE
DCAP_CREATE_MULTIDIMENSIONAL = _gdalconst.DCAP_CREATE_MULTIDIMENSIONAL
DCAP_CREATECOPY = _gdalconst.DCAP_CREATECOPY
DCAP_CREATECOPY_MULTIDIMENSIONAL = _gdalconst.DCAP_CREATECOPY_MULTIDIMENSIONAL
DCAP_MULTIDIM_RASTER = _gdalconst.DCAP_MULTIDIM_RASTER
DCAP_SUBCREATECOPY = _gdalconst.DCAP_SUBCREATECOPY
DCAP_VIRTUALIO = _gdalconst.DCAP_VIRTUALIO
DCAP_RASTER = _gdalconst.DCAP_RASTER
DCAP_VECTOR = _gdalconst.DCAP_VECTOR
DCAP_GNM = _gdalconst.DCAP_GNM
DCAP_NOTNULL_FIELDS = _gdalconst.DCAP_NOTNULL_FIELDS
DCAP_UNIQUE_FIELDS = _gdalconst.DCAP_UNIQUE_FIELDS
DCAP_DEFAULT_FIELDS = _gdalconst.DCAP_DEFAULT_FIELDS
DCAP_NOTNULL_GEOMFIELDS = _gdalconst.DCAP_NOTNULL_GEOMFIELDS
DCAP_NONSPATIAL = _gdalconst.DCAP_NONSPATIAL
DCAP_FEATURE_STYLES = _gdalconst.DCAP_FEATURE_STYLES
DCAP_COORDINATE_EPOCH = _gdalconst.DCAP_COORDINATE_EPOCH
DCAP_MULTIPLE_VECTOR_LAYERS = _gdalconst.DCAP_MULTIPLE_VECTOR_LAYERS
DCAP_FIELD_DOMAINS = _gdalconst.DCAP_FIELD_DOMAINS
DCAP_RENAME_LAYERS = _gdalconst.DCAP_RENAME_LAYERS
DIM_TYPE_HORIZONTAL_X = _gdalconst.DIM_TYPE_HORIZONTAL_X
DIM_TYPE_HORIZONTAL_Y = _gdalconst.DIM_TYPE_HORIZONTAL_Y
DIM_TYPE_VERTICAL = _gdalconst.DIM_TYPE_VERTICAL
DIM_TYPE_TEMPORAL = _gdalconst.DIM_TYPE_TEMPORAL
DIM_TYPE_PARAMETRIC = _gdalconst.DIM_TYPE_PARAMETRIC
CPLES_BackslashQuotable = _gdalconst.CPLES_BackslashQuotable
CPLES_XML = _gdalconst.CPLES_XML
CPLES_XML_BUT_QUOTES = _gdalconst.CPLES_XML_BUT_QUOTES
CPLES_URL = _gdalconst.CPLES_URL
CPLES_SQL = _gdalconst.CPLES_SQL
CPLES_SQLI = _gdalconst.CPLES_SQLI
CPLES_CSV = _gdalconst.CPLES_CSV
GFT_Integer = _gdalconst.GFT_Integer
GFT_Real = _gdalconst.GFT_Real
GFT_String = _gdalconst.GFT_String
GFU_Generic = _gdalconst.GFU_Generic
GFU_PixelCount = _gdalconst.GFU_PixelCount
GFU_Name = _gdalconst.GFU_Name
GFU_Min = _gdalconst.GFU_Min
GFU_Max = _gdalconst.GFU_Max
GFU_MinMax = _gdalconst.GFU_MinMax
GFU_Red = _gdalconst.GFU_Red
GFU_Green = _gdalconst.GFU_Green
GFU_Blue = _gdalconst.GFU_Blue
GFU_Alpha = _gdalconst.GFU_Alpha
GFU_RedMin = _gdalconst.GFU_RedMin
GFU_GreenMin = _gdalconst.GFU_GreenMin
GFU_BlueMin = _gdalconst.GFU_BlueMin
GFU_AlphaMin = _gdalconst.GFU_AlphaMin
GFU_RedMax = _gdalconst.GFU_RedMax
GFU_GreenMax = _gdalconst.GFU_GreenMax
GFU_BlueMax = _gdalconst.GFU_BlueMax
GFU_AlphaMax = _gdalconst.GFU_AlphaMax
GFU_MaxCount = _gdalconst.GFU_MaxCount
GRTT_THEMATIC = _gdalconst.GRTT_THEMATIC
GRTT_ATHEMATIC = _gdalconst.GRTT_ATHEMATIC
GMF_ALL_VALID = _gdalconst.GMF_ALL_VALID
GMF_PER_DATASET = _gdalconst.GMF_PER_DATASET
GMF_ALPHA = _gdalconst.GMF_ALPHA
GMF_NODATA = _gdalconst.GMF_NODATA
GDAL_DATA_COVERAGE_STATUS_UNIMPLEMENTED = _gdalconst.GDAL_DATA_COVERAGE_STATUS_UNIMPLEMENTED
GDAL_DATA_COVERAGE_STATUS_DATA = _gdalconst.GDAL_DATA_COVERAGE_STATUS_DATA
GDAL_DATA_COVERAGE_STATUS_EMPTY = _gdalconst.GDAL_DATA_COVERAGE_STATUS_EMPTY
GARIO_PENDING = _gdalconst.GARIO_PENDING
GARIO_UPDATE = _gdalconst.GARIO_UPDATE
GARIO_ERROR = _gdalconst.GARIO_ERROR
GARIO_COMPLETE = _gdalconst.GARIO_COMPLETE
GTO_TIP = _gdalconst.GTO_TIP
GTO_BIT = _gdalconst.GTO_BIT
GTO_BSQ = _gdalconst.GTO_BSQ


