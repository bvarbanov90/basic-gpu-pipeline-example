import json
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = (
    "basic_2D_GPU_pipeline_example.ipynb",
    "basic_3D_GPU_pipeline_example.ipynb",
    "textured_cube_example.ipynb",
)


class NotebookSmokeTests(unittest.TestCase):
    def test_notebooks_are_valid_version_4_documents(self) -> None:
        for name in NOTEBOOKS:
            with self.subTest(notebook=name):
                notebook = json.loads((REPOSITORY_ROOT / name).read_text(encoding="utf-8"))
                self.assertEqual(notebook["nbformat"], 4)
                self.assertIsInstance(notebook["cells"], list)
                self.assertTrue(notebook["cells"])

    def test_code_cells_compile(self) -> None:
        for name in NOTEBOOKS:
            notebook = json.loads((REPOSITORY_ROOT / name).read_text(encoding="utf-8"))
            for cell_number, cell in enumerate(notebook["cells"], start=1):
                if cell["cell_type"] != "code":
                    continue
                with self.subTest(notebook=name, cell=cell_number):
                    source = "".join(cell["source"])
                    compile(source, f"{name}:cell-{cell_number}", "exec")


if __name__ == "__main__":
    unittest.main()
