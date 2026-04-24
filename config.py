"""config.py v2.1 - relative paths, SimplePod fixes"""
from pathlib import Path

ROOT_DIR = Path(__file__).parent.resolve()
URLS_FILE = ROOT_DIR / "urls.txt"

MODELS_DIR = ROOT_DIR / "models"
WHISPER_MODEL_DIR = MODELS_DIR / "whisper"
QWEN_MODEL_DIR = MODELS_DIR / "qwen_vl"
CLIP_MODEL_DIR = MODELS_DIR / "clip"

OUTPUT_DIR = ROOT_DIR / "output"
VIDEOS_DIR = OUTPUT_DIR / "videos"
AUDIO_DIR = OUTPUT_DIR / "audio"
FRAMES_DIR = OUTPUT_DIR / "frames"
MD_DIR = OUTPUT_DIR / "md"
LOGS_DIR = OUTPUT_DIR / "logs"

VIDEO_FORMAT = "bestvideo[height<=1440][ext=mp4]+bestaudio[ext=m4a]/best[height<=1440]"
DELETE_VIDEO_AFTER_PROCESSING = True
YT_DLP_USER_AGENT = None

WHISPER_MODEL = "large-v3"
WHISPER_LANGUAGE = "en"
WHISPER_DEVICE = "cuda"
WHISPER_COMPUTE_TYPE = "float16"
WHISPER_BEAM_SIZE = 5
USE_VAD_FILTER = True
VAD_MIN_SILENCE_MS = 200
WHISPER_SEGMENT_MODE = "sentence"

FRAME_EXTRACTION_MODE = "interval"
FRAME_INTERVAL_SECONDS = 5
SCENE_CHANGE_THRESHOLD = 0.3
MIN_FRAME_GAP_SECONDS = 3
MAX_FRAMES_PER_VIDEO = 500

FRAME_MAX_DIMENSION = 1920
FRAME_MIN_DIMENSION = 1024
FRAME_SCALE_FLAGS = "lanczos"
FRAME_JPEG_QUALITY = 1

VALIDATE_FRAMES_AFTER_EXTRACT = True

ENABLE_DEDUP = True
DEDUP_MODEL = "openai/clip-vit-large-patch14"
DEDUP_THRESHOLD = 0.92
DEDUP_TIME_WINDOW_SEC = 10
DEDUP_DEVICE = "cuda"
DEDUP_BATCH_SIZE = 16

VISION_MODEL = "Qwen/Qwen2.5-VL-7B-Instruct"
VISION_DEVICE = "cuda"
VISION_DTYPE = "bfloat16"
USE_XFORMERS = True
VISION_MAX_NEW_TOKENS = 250
VISION_BATCH_SIZE = 2

USE_MULTI_GPU = False
USE_QUANTIZATION = False
MAX_MEMORY_PER_GPU = "30GB"

VISION_PROMPT = (
    "You are analyzing a screenshot from a TouchDesigner tutorial video. "
    "Provide a detailed technical description in 2-3 sentences covering: "
    "(1) visible operators with their types (TOP/CHOP/SOP/DAT/MAT/COMP/POP) and names, "
    "(2) connections and network topology, "
    "(3) parameter values visible on screen (exact numbers if readable), "
    "(4) rendered output if present. "
    "Read text on screen precisely (node names, parameter values, menu items). "
    "Do NOT describe the instructor, webcam, or irrelevant background. "
    "Do NOT output code tokens like 'addCriterion', 'Example', 'function'. "
    "If you cannot clearly identify what is on screen, output exactly: [[UNCLEAR]] "
    "Output ONLY the description in plain English, no preamble."
)

VISION_PROMPT_WITH_CONTEXT = (
    "You are analyzing a screenshot from a TouchDesigner tutorial. "
    "At this moment the instructor is saying: \"{context}\"\n\n"
    "Describe whether any operator is visible and if so, which one? "
    "Read the parameters shown on the screen. "
    "Use TouchDesigner terminology. "
    "Do NOT output code tokens like 'addCriterion', 'Example', 'function', or any SQL/Java keywords. "
    "Output ONLY the description in plain English, no preamble, no code."
)

USE_TRANSCRIPT_CONTEXT_FOR_VISION = True

GROUP_INTO_SECTIONS = True
FALLBACK_SECTION_MINUTES = 5
TIMESTAMP_FORMAT = "**[{mm:02d}:{ss:02d}]**"
INCLUDE_METADATA_HEADER = True

SKIP_EXISTING = True
VERBOSE = True


def resolve_path(p):
    """Relative -> absolute using ROOT_DIR. Apsolute -> as is."""
    path = Path(p)
    if path.is_absolute():
        return path
    return ROOT_DIR / path
