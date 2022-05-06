
# Sample Projects

A brief description of what this project does and who it's for





## Demo

Insert gif or link to demo


## Authors

- [@kathir24071997](https://www.github.com/kathir24071997)


## Installation

Install my-project with guthub

```bash
  cd my-project
```
    
## Appendix

Any additional information goes here\
download source code from github
\
\
extract source code 
\
follow given deploye,emt procedure


## Deployment

To deploy this project run

```bash
  install python
  install pip
```
to install pip
```bash
  python -m pip install pip
```
install requirements files
```bash
  pip install requirements.txt
```
migrate projects
```bash
  python manage.py makemigrations
  python manage.py migrate
```
run python server

```bash
  python manage.py runserver
```
## License

[MIT](https://choosealicense.com/licenses/mit/)


## API Reference

####  Post account items

```http
  POST /account/incoming_data
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `email` | **Required**|
| `username` | `string` | **Required** |
| `password` | `password` | **Required** |
| `account` 
| `account_id` | `string` | **Required** |
| `account_name` | `string` | **Required** |
| `website` | `url` | **Option**|

#### Get account item

```http
  GET  /account/incoming_data/${account_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `account_id`      | `string` | **Required**. Id of item to fetch |

#### post destination item

```http
  POST /server/incoming_data
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `account_id` | `string` | **Required** |
| `app_id` | `string` | **Required** |
| `app_name` | `string` | **Required**|
| `app_secret` | `string` | **Required** |
| `app_software` | `string` | **Required** |

#### UPDATE destination item

```http
  PUT  /account/incoming_data/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `app_id` | `string` | **Required** |
| `app_name` | `string` | **Option**|
| `app_secret` | `string` | **Option** |
| `app_software` | `string` | **Option** |

#### get destination item

```http
  GET  /account/incoming_data/${app_id}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `app_id`      | `string` | **Required**. Id of item to fetch |

#### delete account and destination all item

```http
  DELETE  /account/incoming_data/${username,password}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. Id of item to fetch |
| `password`      | `string` | **Required**. Id of item to fetch |

## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform


## 🛠 Skills
python,django,restframework...


## 🚀 About Me
I'm a full stack developer and IoT developer and Embedded developer and Backend developer...

