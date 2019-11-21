## Naming convention

- For .c files: __fw{s, r, t}_{method}.c __where s=standard, r=recursive and t=tiled.
- For folders with results: __{s, r, t}_method/__



## OpenMp

- One Makefile that compiles all source codes.
- All __.c__ files in folder __OpenMp__.
- Result of make in __make__ folders.
- Results of run in __{s, r, t}_method/__ folders.



## tbb

- Separate folder and Makefile for each method.
- In __{s, r, t}_method/__ folders:
  - Makefile
  - Source code
  - Result of make in __make__ folder.
  - Results of run in __results__ folder.



