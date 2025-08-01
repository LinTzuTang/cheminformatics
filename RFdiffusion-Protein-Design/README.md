# RFdiffusion Protein Design Pipeline

This notebook and pipeline are adapted from the original Colab notebook by [Sergey Ovchinnikov (sokrypton)](https://github.com/sokrypton) and the RFdiffusion team.

**Original Colab notebook:**  
[https://colab.research.google.com/github/sokrypton/ColabDesign/blob/v1.1.1/rf/examples/diffusion.ipynb](https://colab.research.google.com/github/sokrypton/ColabDesign/blob/v1.1.1/rf/examples/diffusion.ipynb)

This repository provides an end-to-end pipeline for de novo protein backbone generation, sequence design, and structure validation using **RFdiffusion v1.1.1**, **ProteinMPNN**, and **AlphaFold**.  

---

## Pipeline Overview
1. **Generate novel protein backbone structures using RFdiffusion.**

2. **Use ProteinMPNN to design amino acid sequences that fit the backbone**

3. **Run AlphaFold to predict the final structure from the designed sequence.**


---

## References

- RFdiffusion: [https://github.com/RosettaCommons/RFdiffusion](https://github.com/RosettaCommons/RFdiffusion)
- ProteinMPNN: [https://github.com/dauparas/ProteinMPNN](https://github.com/dauparas/ProteinMPNN)
- AlphaFold: [https://github.com/deepmind/alphafold](https://github.com/deepmind/alphafold)

-