%define module qp_xml

Summary:	Class library to render XML documents from within Python  
Summary(pl):	Modu³ do renderowania domumentów XML przy u¿yciu Pythona  
Name:		python-%{module}
Version:	1.0
Release:	1
License:	Distributable
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Source0:	%{module}-%{version}.tar.gz
#Source0:	http://www.lyra.org/greg/python/qp_xml.py
URL:		http://www.lyra.org/greg/python/
Requires:	python >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	expat

%description
This module provides quick XML documents rendering using expat parser.

%description -l pl
Ten modu³ umo¿liwia szybkie renderowanie dokumentów XML przy u¿yciu
parsera expat.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/python1.5

mv -f *.py $RPM_BUILD_ROOT%{_libdir}/python1.5

%clean
rm -rf $RPM_BUILD_ROOT
					
%files
%defattr(644,root,root,755)
%{_libdir}/python1.5/qp_xml.py
