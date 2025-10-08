# 3ds Max Frame Painting Importer

A tool developed in **Python** with **PySide2** and **pymxs** to automate the import of artworks into **3ds Max**.  
Originally created to streamline the modeling of an exhibition at **Paço Imperial (Rio de Janeiro)** within the **Raul Mourão Art Studio**, this tool simplifies the process of generating framed paintings with real-world dimensions, automatically applying materials and UV mapping from named image files.

---

## English Version (Português abaixo)

### Overview

In gallery and exhibition modeling projects, it's common to deal with dozens (or hundreds) of artwork images. Manually setting up each frame in **3ds Max**—defining dimensions, materials, and textures—can be time-consuming and error-prone.

**3ds Max Frame Importer** automates this entire process:
- Reads **title**, **number**, **height**, and **width** directly from the image filename.
- Creates paintings with **real-world dimensions (in centimeters)**.
- Automatically applies **materials, planar UV mapping**, and the **image texture**.
- Optionally generates **3D frames** with adjustable depth and thickness.
- Includes a **PySide2 graphical interface** for parameter control.

---

### Features

- Automatic import of multiple images (.png, .jpg, .tiff)
- Dimension detection from filename  
  Format: `Title_Number_HeightxWidthCM.jpg`
- Real-world scaling and customizable frame depth
- Automatic material creation and UV mapping
- Simple graphical interface built with **PySide2**
- Compatible with **3ds Max 2023**

---

### Filename Convention

Each image should follow this pattern:

**ArtworkTitle_Number_HeightxWidthCM.jpg**

Example:
Abstract_03_120x90cm.png


Interpreted as:
- Title: "Abstract #03"
- Height: 120 cm
- Width: 90 cm

---

### How to Use

1. Open **3ds Max 2023**.  
2. Ensure Python and PySide2 are enabled.  
3. Run the script via **Scripting > Run Script**.  
4. The **Painting Importer** window will appear.  
5. Select the folder containing the images.  
6. Adjust parameters such as depth and frame thickness.  
7. Click **Import** to generate all paintings automatically.

---

### Technologies

- 3ds Max 2023
- Python 3.7+
- PySide2 (UI)
- pymxs (3ds Max API)
- re, os (Standard libraries)

---

### Motivation

This project was developed during the modeling of **Raul Mourão’s Janelas exhibition** at **Paço Imperial (Rio de Janeiro)**.  
With a library of more than 100 digitized artworks, there was a clear need to automate the 3D import process to optimize the **spatial visualization** and **exhibition planning** workflow.

Though created within an art and architecture context, this project reflects a broader interest in **technical art**, **design automation**, and **creative pipeline optimization**.

---

### Author

**Lucas Vieira Rennó**  
Designer & Technical Artist  
Raul Mourão Studio | Rio de Janeiro, Brazil  
[linkedin.com/in/lucasrenno](https://linkedin.com/in/lucasrenno)

---


## Versão em Português

### Visão Geral

Em projetos de modelagem de galerias e exposições, é comum lidar com dezenas (ou centenas) de imagens de obras. Ajustar manualmente cada uma no **3ds Max** — definindo dimensões, materiais e texturas — é um processo demorado e sujeito a erros.

O **3ds Max Frame Importer** automatiza toda essa etapa:
- Lê automaticamente **título**, **número**, **altura** e **largura** a partir do nome do arquivo.  
- Cria quadros com **dimensões reais (em centímetros)**.  
- Aplica **materiais, mapeamento UV planar** e a **textura da imagem** na face frontal.  
- (Opcional) Gera **molduras tridimensionais** com espessura configurável.  
- Oferece uma **interface gráfica (GUI)** desenvolvida em **PySide2**.

---

### Funcionalidades

- Importação automática de múltiplas imagens (.png, .jpg, .tiff)
- Detecção de dimensões a partir do nome do arquivo  
  Formato: `Titulo_Numero_AlturaXLarguraCM.jpg`
- Escala em centímetros e profundidade configurável
- Criação automática de materiais e mapeamento UV
- Interface gráfica intuitiva com **PySide2**
- Compatível com **3ds Max 2023**

---

### Padrão de Nome de Arquivo

Cada imagem deve seguir o padrão:

**NomeDaObra_Numero_AlturaXLarguraCM.jpg**

Exemplo:

Abstrato_03_120x90cm.png


Interpretado como:
- Título: “Abstrato #03”
- Altura: 120 cm
- Largura: 90 cm

---

### Como Usar

1. Abra o **3ds Max 2023**.  
2. Verifique se o Python e o PySide2 estão habilitados.  
3. Execute o script pelo menu **Scripting > Run Script**.  
4. A janela **Importador de Quadros** será exibida.  
5. Selecione a pasta com as imagens desejadas.  
6. Ajuste parâmetros como profundidade e espessura da moldura.  
7. Clique em **Importar** para gerar automaticamente todos os quadros.

---

### Tecnologias Utilizadas

- 3ds Max 2023  
- Python 3.7+  
- PySide2 (interface)  
- pymxs (integração com o runtime do Max)  
- re, os (bibliotecas padrão)

---

### Motivação

O projeto foi desenvolvido durante a modelagem da exposição "Janelas" de **Raul Mourão** para o **Paço Imperial (RJ)**.  
A partir de uma biblioteca com mais de 100 obras digitalizadas, surgiu a necessidade de automatizar a criação de quadros no ambiente 3D para otimizar o processo de **visualização espacial** e **planejamento expositivo**.

Embora tenha origem no campo das artes visuais, o projeto reflete um interesse mais amplo: a interseção entre **arte, design e tecnologia**, e o papel do **Technical Artist** na otimização de pipelines criativas.

---

### Autor

**Lucas Vieira Rennó**  
Designer & Technical Artist  
Ateliê Raul Mourão | Rio de Janeiro, Brasil  
[linkedin.com/in/lucasrenno](https://linkedin.com/in/lucasrenno)