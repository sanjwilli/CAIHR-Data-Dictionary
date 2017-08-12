# Caribbean Institute of Health Research Data Dictionary

This application is for the Caribbean Instittue of Health Research (CAIHR). This application is for displaying meta data contained with excel files.

## Getting Started

This application uses python flask framework. The data are kept in the folder Data Dictionary. The excel files / data should be held in a folder with it's appropriate project name, for projects that span multiple years they should be placed in folders with the appropriate name with the appropriate year.

## Data Dictionary File and Folder Structure

### Data Dictionary Folder Structure
```
Data Dictionary /
	Project 1
	Project 2
	Project 3
```
### Projects Folder Structure
```
Data Dictionary /
	Project 1 /
		meta data.xlsx
	Project 2 /
		Project 2005
		Project 2006
```

## Prerequites

```
Python 2.7
Flask
```
## Installations

### Python 2.7

```
$ wget --no-check-certificate https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz
$ tar -xzf Python-2.7.11.tgz
$ cd Python-2.7.11
```
You DON'T have to specify Python 2.7.11 you can choose the lastest version of python 2 which is what I highly recommend.