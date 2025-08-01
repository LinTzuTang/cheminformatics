import subprocess
import os

def run_rfdiffusion(model_ckpt, seq_length, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)
    backbone_path = os.path.join(output_dir, "backbone.pdb")
    cmd = [
        "python", "scripts/run_inference.py",  # 範例，根據實際 RFdiffusion 指令修改
        "--model", model_ckpt,
        "--length", str(seq_length),
        "--out_dir", output_dir
    ]
    print("Running RFdiffusion:", " ".join(cmd))
    subprocess.run(cmd, check=True)
    return backbone_path

def run_protein_mpnn(backbone_path, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)
    seq_path = os.path.join(output_dir, "designed_sequence.fasta")
    cmd = [
        "python", "protein_mpnn_run.py",  # 範例
        "--structure", backbone_path,
        "--out_dir", output_dir
    ]
    print("Running ProteinMPNN:", " ".join(cmd))
    subprocess.run(cmd, check=True)
    return seq_path

def run_alphafold(seq_path, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)
    af2_path = os.path.join(output_dir, "af2_struct.pdb")
    cmd = [
        "python", "run_alphafold.py",  # 範例
        "--fasta", seq_path,
        "--out_dir", output_dir
    ]
    print("Running AlphaFold:", " ".join(cmd))
    subprocess.run(cmd, check=True)
    return af2_path
