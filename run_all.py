"""
run_all.py v2 - Run all stages in sequence (with optional dedup)
"""
import sys
import subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import config

STAGES = [
    ('Stage 1: Download + Frame extraction', 'stage1_download.py'),
    ('Stage 2: faster-whisper transcription', 'stage2_transcribe.py'),
]
if config.ENABLE_DEDUP:
    STAGES.append(('Stage 2b: CLIP dedup', 'stage2b_dedup.py'))
STAGES += [
    ('Stage 3: Qwen2.5-VL descriptions', 'stage3_vision.py'),
    ('Stage 4: Assemble .md files', 'stage4_assemble.py'),
]


def main():
    script_dir = Path(__file__).parent
    for name, script in STAGES:
        print(f"\n{'#'*70}")
        print(f"# {name}")
        print(f"{'#'*70}\n")
        result = subprocess.run([sys.executable, str(script_dir / script)], cwd=str(script_dir))
        if result.returncode != 0:
            print(f"\nGRESKA u {script}, prekidam.")
            sys.exit(1)
    print("\n" + "="*70)
    print("DONE. Final .md in output/md/")
    print("="*70)


if __name__ == '__main__':
    main()
