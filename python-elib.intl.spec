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
BuildRequires:	python2-setuptools
BuildRequires:	python2-sphinx
Provides:	%{oname} = %{version}-%{release}

%description
The elib.intl module provides enhanced internationalization (I18N) services
for your Python modules and applications.

elib.intl wraps Python's :func:`gettext` functionality.

%prep
%setup -qn %{oname}-%{gdate}

%build
python2 setup.py build

pushd doc/reference
        make html SPHINXBUILD=sphinx-build2
	rm -rf build/html/.buildinfo
popd

%install
python2 setup.py install \
	--root %{buildroot}

%files
%doc doc/reference/build/html
%{py2_puresitedir}/%{oname}*
%{py2_puresitedir}/elib/


