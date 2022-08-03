<link rel="stylesheet" type="text/css" media="all" href="style.css" />

<h1 align="center">
    <a class="anim-pulse" href="https://animax.com"><img src="https://raw.githubusercontent.com/emarc99/Huddle-Landing-Page/main/images/animax.js.jpeg" width="175px" alt="< animax.js >"></a>
</h1>

<h1 align="center">Zuri Team 098
</h1>

---

<p align="center">Built with the sole purpose of making life easier for beginner web developers.
</p>

<p align="center">
 <a href="#contributing">
   <img src="https://img.shields.io/github/issues/zuri-training/anima_lib_team98" alt="Issues">
 </a>
 <a href="https://github.com/zuri-training/anima_lib_team98/discussions">
  <img src="https://img.shields.io/github/contributors/zuri-training/anima_lib_team98" alt="Discussions">
 </a>
 <a href="https://github.com/cdnjs/animax/blob/master/LICENSE">
  <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg?style=flat-square" alt="MIT License">
 </a>
</p>

---

## Table of Contents


- [Table of Contents](#table-of-contents)
- [Technologies Used](#technologies-used)
- [Resources/Links](#resourceslinks)
- [Introduction](#introduction)
  - [Getting Started](#getting-started)
  - [Features](#features)
  - [Animations](#animations)
- [Usage Examples](#usage-examples)
- [Interactive Animations](#interactive-animations)
- [Development](#development)
- [Contributing](#contributing)
- [Sponsors](#sponsors)
- [License](#license)

## Technologies Used
- HTML
- CSS
- JavaScript
- Python (Django)
- MySQL

## Resources/Links
 - [Animax Web Application](animax-js-css.com)
 - [Figma](https://www.figma.com/file/mnP49B5GDsVrVBPIp1Q6g0/Animax-Project-Design?node-id=604%3A980)
 - [Database Schema](https://figma.com)
 - [First Presentation](https://drive.google.com/file/d/1RhV8apcyZNm-udaeVtNrwc2EhNOslGLj/view?usp=sharing)
 - [Second Presentation](https://figma.com)
 - [Meetings' Minutes](docs.google.com)
 - [List of Accomplished Tasks](https://docs.google.com/spreadsheets/d/1hxQbE1XdJ99-JEQI5cQ6hj8YUqHRTQ0KgzNLgOPfWa8/edit#gid=1652708415)

## Introduction

Animax is a simple animation library that allows users to perform basic web animation using little to no code.

### Getting Started

Velit sapien, venenatis arcu ut quam. Risus pellentesque mauris, etiam at vitae nibh. Vulputate vulputate consequat venenatis eleifend eu sagittis ut pretium non.

Go through the [DOCUMENTATION.md](https://github.com/zuri-training/anima_lib_team98/blob/develop/DOCUMENTATION.md) for the full animax library documentation.

### Features

- Normal language: The name of the animations are very close to normal human language, and user do not need to write any code at all.

- Easy-to-use: Just apply the ID (i.e. the CSS selector) of the animation you want.

- Light and user-friendly: The library was built using plain CSS, and no use of external libraries.

### Animations

At this time, the library has the following animations:
- Alternate colors
- Blink
- Bounce
- Fade
- Move
- Pulse
- Rotate
- Stretch

## Usage Examples

1. Download the library.
2. Extract the zipped file.
3. Import the library into your project using the <code>link</code> tag. 
   
   ```html
   <html>
   <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="animax.css">
    
    <title>Home</title>
   </head>
   <body>
   
    ........

    <script src="animax.js"></script>
   </body>
   </html>
   ```

4. Add the animation ID, which is <code>bounce-1x"</code> in this instance, to the HTML element you would like to animate.
   ```html
   <body>
   
    ........
 
   
   <div id="bounce-1x"></div>

    ........

   </body>
   ```

5. Voila, the element is automatically animated.
   
   <div class="animation-row">
    <div id="bounce-1x" class="circle"></div>
   </div>
        
        

## Interactive Animations

JavaScript Web Animations API is used to create the experience for users to generate their preferred code combinations. This feature is made for users that want more granularity and control over their animations. This solution is implemented with plain JavaScript (no external libraries) so as to provide the best performance and a good starting point for developers to learn about creating interactive animation.
 - Minimum Requirement: Understand the basics of JS and programming in general. Knowledge of JS WAAPI is not required.
 - Reasons:  No need to rely on DOM-heavy manipulation techniques.

## Development

See [DEVELOP.md](https://github.com/zuri-training/anima_lib_team98/blob/develop/DEVELOPMENT.md) for development docs.

## Contributing


|      Designers     |     Developers    | 
|         :---:      |       :----:      |
|  Tobechukwu Eloke  | Charles Precious  |
|     Tomi Etta      | Mustapha Balogun  |
|  Zainab Bodude     |  Aroso Emmanuel Adedeji |
|   Khadijat Bakare  |    Solomon Ezeatum |
|   Coker Adebusola  |   David Alatishe   |
|   Victor Roosevelt |  Oluji Onyekachukwu |
|     Fatoye Ruth    | Oguagu Ekenechukwu Daniel  |
| Aminu Musa Ambursa | Francois Pape Diouf  |
| Olamilekan Phillip |  
| Joshua Opeyemi Adebisi |  
| Salau Shukurat |  

## Sponsors

Animax project would neither have been realized nor be the success that it is today without our sponsors' kind support. These organizations currently support animax:

* [Ingresive 4 Good](https://ingressive.org/)
* [Zuri Team](https://training.zuri.team)

## License

[MIT license](https://github.com/zuri-training/anima_lib_team98/blob/develop/LICENSE) ©2022
