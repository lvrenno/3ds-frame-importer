import os
import re
from pymxs import runtime as rt
from PySide2 import QtWidgets, QtCore

# Extrai título, número, altura e largura do nome do arquivo
def extract_info(filename):
    match = re.match(r"(.+?)_(\d+)_([\d]+)x([\d]+)cm", filename)
    if match:
        title = match.group(1)
        number = match.group(2)
        height = float(match.group(3))
        width = float(match.group(4))
        return f"{title} #{number}", height, width
    return None, None, None

# Cria a moldura como uma caixa com profundidade atrás do quadro
def create_frame(height, width, thickness, depth, title):
    frame_height = height + 2 * thickness
    frame_width = width + 2 * thickness

    # Cria a moldura como uma caixa (Box)
    frame = rt.Box(length=frame_height, width=frame_width, height=depth, name=f"{title}_frame")
    frame.pos = rt.Point3(0, 0, depth / 2 - 0.1)  # Posiciona atrás do quadro

    # Aplica cor preta à moldura
    frame_material = rt.StandardMaterial()
    frame_material.diffuse = rt.color(0, 0, 0)
    frame.material = frame_material

    # Converte para Editable Poly
    rt.convertToPoly(frame)

    return frame

# Cria o quadro
def create_painting(image_path, title, height_cm, width_cm, depth_cm, add_frame, frame_thickness_cm):
    height = height_cm
    width = width_cm
    depth = depth_cm

    # Cria o quadro como uma caixa
    box = rt.Box(length=height, width=width, height=depth, name=title)
    box.pos = rt.Point3(0, 0, depth / 2)

    # Converte para Editable Poly (em vez de Mesh)
    rt.convertToPoly(box)

    # Define material IDs: face de cima = 1, outras = 2
    num_faces = rt.polyOp.getNumFaces(box)
    for i in range(1, num_faces + 1):
        normal = rt.polyOp.getFaceNormal(box, i)
        if normal.z > 0.99:
            rt.polyOp.setFaceMatID(box, i, 1)
        else:
            rt.polyOp.setFaceMatID(box, i, 2)

    # Aplica mapeamento UVW (compatível com Editable Poly)
    uvw = rt.UVWMap()
    uvw.mappingType = rt.Name("planar")
    uvw.length = height
    uvw.width = width
    uvw.height = depth
    uvw.align = rt.Name("z")
    rt.addModifier(box, uvw)

    # Cria textura da imagem
    texture = rt.Bitmaptexture()
    texture.filename = image_path
    texture.tileU = False
    texture.tileV = False

    # Material da imagem
    mat_image = rt.StandardMaterial()
    mat_image.diffuseMap = texture

    # Material neutro (preto)
    mat_black = rt.StandardMaterial()
    mat_black.diffuse = rt.color(0, 0, 0)

    # Multi/Sub-Object Material
    multi_mat = rt.MultiMaterial()
    multi_mat.materialList = rt.array(mat_image, mat_black)
    multi_mat.names = rt.array("Top", "Other")
    multi_mat.numSubs = 2

    box.material = multi_mat

    # Cria moldura se necessário
    if add_frame:
        frame = create_frame(height, width, frame_thickness_cm, depth, title)
        group = rt.group([frame, box], name=f"{title}_group")
        return group
    else:
        return box

# Widget de configuração de cada obra
class PaintingWidget(QtWidgets.QWidget):
    def __init__(self, filename, image_path, title, height, width):
        super().__init__()
        self.image_path = image_path
        self.title = title
        self.height = height
        self.width = width

        layout = QtWidgets.QHBoxLayout()

        # Layout para checkbox de habilitado + título
        title_layout = QtWidgets.QHBoxLayout()
        self.enable_checkbox = QtWidgets.QCheckBox()
        self.enable_checkbox.setChecked(True)
        self.enable_checkbox.stateChanged.connect(self.toggle_enabled_fields)

        self.label = QtWidgets.QLabel(title)
        self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        title_layout.addWidget(self.enable_checkbox)
        title_layout.addWidget(self.label)
        title_layout.addStretch()

        # Checkbox de moldura
        self.frame_checkbox = QtWidgets.QCheckBox("Moldura?")
        self.frame_checkbox.setChecked(False)
        self.frame_checkbox.stateChanged.connect(self.toggle_thickness_input)

        # Campo de espessura da moldura
        self.thickness_input = QtWidgets.QLineEdit("2.0")
        self.thickness_input.setFixedWidth(50)
        self.thickness_input.setEnabled(False)

        # Campo de profundidade
        self.depth_input = QtWidgets.QLineEdit("5.0")
        self.depth_input.setFixedWidth(50)

        # Adiciona os layouts e widgets ao layout principal
        layout.addLayout(title_layout)
        layout.addWidget(self.frame_checkbox)
        layout.addWidget(QtWidgets.QLabel("Espessura da moldura (cm):"))
        layout.addWidget(self.thickness_input)
        layout.addWidget(QtWidgets.QLabel("Profundidade (cm):"))
        layout.addWidget(self.depth_input)

        self.setLayout(layout)

    def toggle_thickness_input(self, state):
        self.thickness_input.setEnabled(state == QtCore.Qt.Checked and self.enable_checkbox.isChecked())

    def toggle_enabled_fields(self, state):
        enabled = state == QtCore.Qt.Checked
        self.frame_checkbox.setEnabled(enabled)
        self.thickness_input.setEnabled(enabled and self.frame_checkbox.isChecked())
        self.depth_input.setEnabled(enabled)

    def get_config(self):
        try:
            thickness = float(self.thickness_input.text())
        except:
            thickness = 2.0
        try:
            depth = float(self.depth_input.text())
        except:
            depth = 5.0
        return {
            "enabled": self.enable_checkbox.isChecked(),
            "image_path": self.image_path,
            "title": self.title,
            "height": self.height,
            "width": self.width,
            "add_frame": self.frame_checkbox.isChecked(),
            "thickness": thickness,
            "depth": depth
        }

# Interface principal
class PaintingImporter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Importador de Quadros")
        self.setMinimumSize(600, 400)

        self.layout = QtWidgets.QVBoxLayout()

        path_layout = QtWidgets.QHBoxLayout()
        self.path_input = QtWidgets.QLineEdit()
        browse_btn = QtWidgets.QPushButton("Selecionar")
        browse_btn.clicked.connect(self.browse_folder)
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(browse_btn)

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout()
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)

        self.import_btn = QtWidgets.QPushButton("Importar")
        self.import_btn.clicked.connect(self.import_paintings)

        self.layout.addLayout(path_layout)
        self.layout.addWidget(self.scroll_area)
        self.layout.addWidget(self.import_btn)
        self.setLayout(self.layout)

        self.painting_widgets = []

    def browse_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Selecionar Pasta")
        if folder:
            self.path_input.setText(folder)
            self.load_paintings(folder)

    def load_paintings(self, folder):
        self.painting_widgets.clear()
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        for file in os.listdir(folder):
            name, ext = os.path.splitext(file)
            if ext.lower() in ['.jpg', '.png', '.tiff']:
                title, height, width = extract_info(name)
                if title and height and width:
                    image_path = os.path.join(folder, file)
                    painting_widget = PaintingWidget(name, image_path, title, height, width)
                    self.scroll_layout.addWidget(painting_widget)
                    self.painting_widgets.append(painting_widget)

    def import_paintings(self):
        imported = 0
        for painting_widget in self.painting_widgets:
            config = painting_widget.get_config()
            if config["enabled"]:
                create_painting(
                    config["image_path"],
                    config["title"],
                    config["height"],
                    config["width"],
                    config["depth"],
                    config["add_frame"],
                    config["thickness"]
                )
                imported += 1

        if imported == 0:
            rt.messageBox("Nenhum quadro selecionado para importação.")
        else:
            rt.messageBox(f"Importação concluída com sucesso! {imported} quadro(s) importado(s).")

# Executa a interface
app = QtWidgets.QApplication.instance()
if not app:
    app = QtWidgets.QApplication([])
window = PaintingImporter()
window.show()