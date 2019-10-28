#
# Conditional build:
%bcond_with	doc	# do build doc (missing deps)
%bcond_with	tests	# do perform "make test" (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	OpenStack Block Storage API Client Library
Name:		python-cinderclient
Version:	3.1.0
Release:	3
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/python-cinderclient/%{name}-%{version}.tar.gz
# Source0-md5:	476881992a4b28b458a513dea61fb17f
URL:		https://pypi.python.org/pypi/python-cinderclient
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-babel >= 2.3.4
Requires:	python-keystoneauth1 >= 3.0.1
Requires:	python-oslo.i18n >= 2.1.0
Requires:	python-oslo.utils >= 3.20.0
Requires:	python-pbr >= 2.0.0
Requires:	python-prettytable >= 0.7.1
Requires:	python-simplejson >= 2.2.0
Requires:	python-six >= 1.9.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a client for the OpenStack Cinder API. There's a Python API
(the cinderclient module), and a command-line script (cinder). Each
implements 100% of the OpenStack Cinder API.

%package -n python3-cinderclient
Summary:	OpenStack Block Storage API Client Library
Group:		Libraries/Python
Requires:	python3-babel >= 2.3.4
Requires:	python3-keystoneauth1 >= 3.0.1
Requires:	python3-oslo.i18n >= 2.1.0
Requires:	python3-oslo.utils >= 3.20.0
Requires:	python3-prettytable >= 0.7.1
Requires:	python3-simplejson >= 2.2.0
Requires:	python3-six >= 1.9.0

%description -n python3-cinderclient
This is a client for the OpenStack Cinder API. There's a Python API
(the cinderclient module), and a command-line script (cinder). Each
implements 100% of the OpenStack Cinder API.

%package -n cinderclient
Summary:	OpenStack Block Storage API Client
Group:		Applications
%if %{with python3}
Requires:	python3-cinderclient = %{version}-%{release}
%else
Requires:	%{name} = %{version}-%{release}
%endif

%description -n cinderclient
This is a client for the OpenStack Cinder API.

%package apidocs
Summary:	API documentation for Python cinderclient module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona cinderclient
Group:		Documentation

%description apidocs
API documentation for Pythona cinderclient module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona cinderclient.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/cinderclient
%{py_sitescriptdir}/python_cinderclient-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-cinderclient
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/cinderclient
%{py3_sitescriptdir}/python_cinderclient-%{version}-py*.egg-info
%endif

%files -n cinderclient
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%attr(755,root,root) %{_bindir}/cinder

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
