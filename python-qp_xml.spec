%include	/usr/lib/rpm/macros.python

%define module qp_xml

Summary:	Class library to render XML documents from within Python
Summary(pl):	Modu� do renderowania dokument�w XML przy u�yciu Pythona
Name:		python-%{module}
Version:	1.0
Release:	3
License:	distributable
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(es):	Desarrollo/Lenguages/Python
Group(fr):	Development/Langues/Python
Group(pl):	Programowanie/J�zyki/Python
Group(pt):	Desenvolvimento/L�nguas/Python
Source0:	%{module}-%{version}.tar.gz
#Source0:	http://www.lyra.org/greg/python/qp_xml.py
URL:		http://www.lyra.org/greg/python/
Requires:	expat
%requires_eq	python
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides quick XML documents rendering using expat parser.

%description -l pl
Ten modu� umo�liwia szybkie renderowanie dokument�w XML przy u�yciu
parsera expat.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

install *.py $RPM_BUILD_ROOT%{py_sitedir}

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT
					
%files
%defattr(644,root,root,755)
%{py_sitedir}/*.py?
