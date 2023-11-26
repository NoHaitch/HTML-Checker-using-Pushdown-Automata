<!-- Back to Top Link-->
<a name="readme-top"></a>


<br />
<div align="center">
  <h1 align="center">Tugas Besar IF2124 Teori Bahasa Formal dan Otomata</h1>

  <p align="center">
    <h3> HTML Checker using Pushdown Automata (PDA)</h3>
    <p>on Python langguage</p>
    <br />
    <a href="https://github.com/zultopia/Tubes-IF2124-TBFO/issues">Report Bug</a>
    ·
    <a href="https://github.com/zultopia/Tubes-IF2124-TBFO/issues">Request Feature</a>
<br>
<br>

[![MIT License][license-shield]][license-url]

  </p>
</div>

<!-- CONTRIBUTOR -->
<div align="center" id="contributor">
  <strong>
    <h3>Dibuat oleh Kelompok Otax Error :</h3>
    <table align="center">
      <tr>
        <td>NIM</td>
        <td>Nama</td>
      </tr>
      <tr>
        <td>13522070</td>
        <td>Marzuli Suhada M</td>
      </tr>
      <tr>
        <td>13522071</td>
        <td>Bagas Sambega Rosyada</td>
      </tr>
      <tr>
        <td>13522091</td>
        <td>Raden Francisco Trianto Bratadiningrat</td>
      </tr>
    </table>
  </strong>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#installation--getting-started">Installing / Getting Started</a>
    </li>
    <li><a href="#developing">Developing</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#links">Links</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## External Links

- [Repository](https://github.com/zultopia/Tubes-IF2124-TBFO/)
- [Link Spesifikasi](https://docs.google.com/document/d/1W5QSSHVrXvArj3Aonw4FhbfctBK6J2YGefXpWsLW43Y/edit)
- [Link Q&A](https://docs.google.com/spreadsheets/d/1g3IBzFkH1edkMHGrsCAsjYFQD8APkmrxhBAUQj7sXBk/edit#gid=0)
- [Link Data Kelompok](https://docs.google.com/spreadsheets/d/10BsoEnc5gNOecG3WAjynOeTsL86Llrup34aQoojYOhU/edit#gid=318288469)


<!-- ABOUT THE PROJECT -->
## About The Project

To further develop our knowledge in Automata Langguage in IF2124 Theory of Formal Langguage and Automata course, we were given the task to make a HTML checker using PDA with the help of Python. The main checker will be the PDA not using hardcoded Regex in Python. 

PDA in Python used as reference : https://github.com/theodoregold/pushdown-automata

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Installation / Getting Started

1. Clone the repo
   ```sh
   git clone https://github.com/zultopia/Tubes-IF2124-TBFO
   ```
2. Change directory to src
   ```sh
   cd src
   ```
3. Run the program
   ```sh
   python main.py main.txt [html.txt]
   # main.txt is the PDA for the checker
   # html.txt is the html file that is checked
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FEATURES -->
## Features

### 1. List of tag checked
  - html
  - head
  - body
  - title
  - link
  - script
  - h1, h2, h3, h4, h5, h6
  - p
  - br
  - hr
  - div
  - a
  - img
  - button
  - form
  - input
  - table
  - tr
  - td
  - th

## 2. Tag with nested
  - html
  - body
  - head
   - div
  - form
  - table

## 3. Formating element tag
  - em
  - b
  - abbr
  - strong
  - small


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are __warmly welcome__.

Jika Anda ingin berkontribusi atau melanjutkan perkembangan program, silahkan fork repository ini dan gunakan branch fitur. Permintaan Pull __sangat diperbolehkan dan diterima dengan hangat__.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Links
- Project homepage: https://github.com/zultopia/Tubes-IF2121-Logika-Komputasional
- Repository: https://github.com/zultopia/Tubes-IF2121-Logika-Komputasional
- Issue tracker: https://github.com/zultopia/Tubes-IF2121-Logika-Komputasional/issues

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## Licensing

The code in this project is licensed under MIT license.  
Code dalam projek ini berada di bawah lisensi MIT.



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<br>
<h3 align="center"> THANK YOU! </h3>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-url]: https://github.com/zultopia/Tubes-IF2124-TBFO/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/zultopia/Tubes-IF2124-TBFO/blob/main/LICENSE
