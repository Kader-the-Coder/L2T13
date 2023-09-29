<a name="readme-top"></a>
<br />
<div align="center">
  <a href="https://github.com/Kader-the-Coder/book-manager">
    <img src="images/book_icon.png" alt="Logo" width="80" height="80">
  </a>
<h3 align="center">Book Manager</h3>
  <p align="center">
    Manages books using sqlite3
  </p>
</div>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

## About The Project
<span style="display:block;text-align:center">![screenshot1]</span>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

Program for a bookstore. This program allow a clerk to enter data about
new books into the database, update book information, delete books from
the database, and search to find the availability of books in the
database.

## Getting Started

In order to make use of this project, follow the steps below:


### Prerequisites

```sh
Any code editor
```

### Installation

Just clone the repo
   ```sh
   git clone
   https://github.com/github_username/repo_name.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Usage

This program can be used to enter an new book, update and existing book, delete an existing book or search for a book in the database.
###
<span style="display:block;text-align:center">![screenshot2]</span>
- Entering a book
```
When entering a book, simply input a title and author name
```
<span style="display:block;text-align:center">![screenshot3]</span>
###
- Update a book
```
All fields of a book can be updated (except the book id). Simply search for a book and input the field that you would want change, followed by the value you would like to change it to. The option to update a book will only be available if your search text matches ONE book. (Recommended to search via book id)
```
- Delete a book
```
To delete a book, first search for the book you want to delete. The option to delete a book will only be available if your search text matches ONE book. (Recommended to search via book id)
```
- Search for a book
```
To search for a book, input the search text that you are looking for. The program will search for the text in all fields of the database. All books which contains the search text will be returned. To refine your search, you can use the '@' operator, followed by the field name to search in a specified field.
```
<span style="display:block;text-align:center">![screenshot4]</span>
###
<span style="display:block;text-align:center">![screenshot5]</span>
###
You are able to return to the main menu at any time by raising a keyboard interrupt error, i.e. by pressing: ```CTRL+C```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## License

None
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[screenshot1]: images/screenshot1.png
[screenshot2]: images/screenshot2.png
[screenshot3]: images/screenshot3.png
[screenshot4]: images/screenshot4.png
[screenshot5]: images/screenshot5.png
