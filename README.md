# 3ds Max Frame Importer (Editable Poly Version)

A Python tool built with **PySide2** and **pymxs** to automate the creation of framed paintings in **3ds Max**.  
Developed to streamline exhibition modeling at the **Raul Mourão Art Studio**, this script imports artwork images with real-world dimensions, applies textures and UV mapping, and procedurally builds adjustable 3D frames.

---

## English Version (Português abaixo)

### Overview

When working with galleries or exhibitions, managing multiple artworks in **3ds Max** can become repetitive — manually scaling, texturing, and framing each painting.  
**3ds Max Frame Importer Builder** automates this workflow through a simple interface that reads image dimensions from filenames and generates fully configured 3D paintings.

This updated 3ds Max Painting Importer automates the entire process using Editable Poly geometry, offering greater flexibility for further modeling, editing, or deformation.

---

### Features

- Automatic import of multiple image formats: `.png`, `.jpg`, `.tif`
- Reads artwork dimensions directly from the filename  
  Format: `Title_Number_HeightxWidthCM.jpg`
- Creates geometry in **real-world scale (centimeters)**
- Uses Editable Poly objects instead of meshes.
- Applies materials and **planar UV mapping**, and the image texture.
- Optionally generates 3D frames with adjustable thickness and depth.
- Intuitive **PySide2 GUI** for parameter control
- Compatible with **3ds Max 2023 and 2024**

---

### Filename Convention

Each image file should follow this pattern:

**ArtworkTitle_Number_HeightxWidthCM.jpg**

Example:  
`Abstract_03_120x90cm.png`

Interpreted as:
- Title: “Abstract #03”  
- Height: 120 cm  
- Width: 90 cm  

---

### How to Use

1. Open **3ds Max 2023 or 2024**.  
2. Ensure Python and PySide2 are active.  
3. Run the script via **Scripting > Run Script**.  
4. The **Frame Importer Builder** window will appear.  
5. Select a folder with artwork images.  
6. Adjust depth, frame thickness, or disable frame generation.  
7. Click **Import** to automatically create and texture all paintings.

---

### Technologies

- 3ds Max 2023–2024  
- Python 3.7+  
- PySide2 (GUI)  
- pymxs (3ds Max runtime API)  
- re, os (standard libraries)

---

### Motivation

Originally designed for the modeling of **Raul Mourão’s exhibition “Janelas”** at **Paço Imperial (Rio de Janeiro)**, this tool reduced the repetitive manual setup of over 100 artworks.  
The project embodies a broader exploration of **technical art**, **creative coding**, and **automation in design workflows**.

This Editable Poly version represents a technical refinement of that goal — aligning with best practices in 3ds Max modeling and expanding the script’s use beyond art spaces into architectural visualization, technical art, and design automation.

---

### Author

**Lucas Vieira Rennó**  
Designer & Technical Artist  
Raul Mourão Studio | Rio de Janeiro, Brazil  
[linkedin.com/in/lucasrenno](https://linkedin.com/in/lucasrenno)

---

## Versão em Português

### Visão Geral

Ao trabalhar com modelagem de galerias e exposições, ajustar manualmente cada quadro no **3ds Max** — definindo escala, textura e moldura — é um processo repetitivo e demorado.  
O **3ds Max Frame Importer Builder** automatiza essa tarefa a partir de uma interface simples, lendo dimensões diretamente do nome do arquivo e criando quadros 3D completos.

Esta versão atualizada do 3ds Max Painting Importer automatiza toda essa etapa, agora utilizando Editable Poly em vez de Editable Mesh, garantindo maior controle geométrico e compatibilidade com modificadores e workflows de modelagem.

---

### Funcionalidades

- Importação automática de múltiplos formatos de imagem: `.png`, `.jpg`, `.tif`
- Lê as dimensões da obra diretamente a partir do nome do arquivo
- Formato: `Titulo_Numero_AlturaxLarguraCM.jpg`
- Cria geometria em **escala real (centímetros)**
- Utiliza objetos **Editable Poly** em vez de malhas (meshes)
- Aplica materiais, **mapeamento UV planar** e a textura da imagem
- Gera opcionalmente **molduras 3D** com espessura e profundidade ajustáveis
- Interface intuitiva em **PySide2** para controle dos parâmetros
- Compatível com **3ds Max 2023 e 2024**

---

### Padrão de Nome de Arquivo

Cada imagem deve seguir o padrão:

**NomeDaObra_Numero_AlturaxLarguraCM.jpg**

Exemplo:  
`Abstrato_03_120x90cm.png`

Interpretado como:
- Título: “Abstrato #03”  
- Altura: 120 cm  
- Largura: 90 cm  

---

### Como Usar

1. Abra o **3ds Max 2023 ou 2024**.  
2. Verifique se o Python e o PySide2 estão habilitados.  
3. Execute o script pelo menu **Scripting > Run Script**.  
4. A janela **Frame Importer Builder** será exibida.  
5. Selecione a pasta com as imagens.  
6. Ajuste profundidade, espessura da moldura ou desative-a.  
7. Clique em **Importar** para gerar automaticamente todos os quadros.

---

### Tecnologias Utilizadas

- 3ds Max 2023–2024  
- Python 3.7+  
- PySide2 (interface gráfica)  
- pymxs (API de integração com o Max)  
- re, os (bibliotecas padrão)

---

### Motivação

Desenvolvido durante a modelagem da exposição **“Janelas” de Raul Mourão** no **Paço Imperial (RJ)**, o script surgiu para eliminar a repetição de tarefas na criação de mais de 100 quadros.  
O projeto reflete um interesse em **automação criativa**, **arte generativa** e na atuação do **Technical Artist** como elo entre **arte e tecnologia**.

Esta versão em **Editable Poly** representa um aprimoramento técnico desse objetivo — alinhando-se às boas práticas de modelagem no **3ds Max** e ampliando o uso do script para além dos espaços artísticos, abrangendo também **visualização arquitetônica**, **arte técnica (Technical Art)** e **automação de design**.

A versão usando Editable Poly representa uma evolução técnica do projeto, permitindo maior compatibilidade com ferramentas de modelagem e fluxos criativos que exigem precisão e flexibilidade — alinhando arte, design e tecnologia sob a ótica do Technical Artist.

---

### Autor

**Lucas Vieira Rennó**  
Designer & Technical Artist  
Ateliê Raul Mourão | Rio de Janeiro, Brasil  

[linkedin.com/in/lucasrenno](https://linkedin.com/in/lucasrenno)
