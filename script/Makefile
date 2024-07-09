.PHONY: all setup download unzip clean

all: setup download unzip clean

setup:
	pip install -r ../requirements.txt

download:
	mkdir -p ../dataset
	kaggle datasets download -d mehyarmlaweh/ner-annotated-cvs -p ../dataset

unzip:
	unzip -o ../dataset/ner-annotated-cvs.zip -d ../dataset

clean:
	rm ../dataset/ner-annotated-cvs.zip
