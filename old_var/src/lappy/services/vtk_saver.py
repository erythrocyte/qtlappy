#!/usr/bin/env python3
# coding: utf-8

def save_vtk(fn: str, vtkn: str, dtn: str, pts, seg):
    """
    save geometry as vtk file

    args:
        fn(str) : file name
        vtkn (str) : vtk global name
        dtn(str): data name
        pts (list) : points
        seg (list) : segments
    """

    with open(fn, 'w') as f:
        f.write('# vtk DataFile Version 3.0\n')
        f.write(f'{ vtkn }\n')
        f.write('ASCII\n')
        f.write('DATASET UNSTRUCTURED_GRID\n')

        # --- points count
        f.write(f'POINTS { len(pts) } double\n')

        # ---- nodes
        for pt in pts:
            f.write(f'{ pt[0] } { pt[1]} 0.0\n')

        # ---- cells count
        f.write(f'CELLS { len(seg) } { len(seg) * 3 }\n')

        # ---- cells
        for sg in seg:
            f.write(f'{ len(sg) }\t{ sg[0] } { sg[1] }\n')

        # ---- cells type
        f.write(f'CELL_TYPES {len(seg)}\n')  # cell type header
        f.write('3\n'*len(seg))  # cell types

        # --- cells data
        f.write(f'CELL_DATA { len(seg) }\n')

        f.write(f'SCALARS { dtn } float 1\n')
        f.write('LOOKUP_TABLE default\n')
        for i in range(len(seg)):
            f.write(f'{i}\n')
