%define oname	elib.intl

%define gdate	20110711

Name:		python-%{oname}
Version:	0.0.3
Release:	0.%{gdate}.1
Summary:	Enhanced internationalization (I18N) for Python
License:	LGPLv3+
Group:		Development/Python
Url:		https://github.com/dieterv/elib.intl
Source0:	%{oname}-%{gdate}.tar.xz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx
Provides:	%{oname} = %{version}-%{release}

%description
The elib.intl module provides enhanced internationalization (I18N) services
for your Python modules and applications.

elib.intl wraps Python's :func:`gettext` functionality.

%prep
%setup -qn %{oname}-%{gdate}

%build
python setup.py build

pushd doc/reference
        make html
	rm -rf build/html/.buildinfo
popd

%install
python setup.py install \
	--root %{buildroot}

%files
%doc doc/reference/build/html
%{py_puresitedir}/%{oname}*
%{py_puresitedir}/elib/


