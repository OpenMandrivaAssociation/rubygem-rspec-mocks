%define oname rspec-mocks
%define geminstdir %{ruby_gemdir}/gems/%{oname}-%{version}

Summary:    Behaviour Driven Development for Ruby
Name:       rubygem-%{oname}
Version:    2.8.0
Release:	3
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/rspec/rspec-mocks
Source0:    %{oname}-%{version}.gem
Requires:   rubygems
Requires:   rubygem(rspec-core)
Requires:   rubygem(rspec-expectations)
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
RSpec's 'test double' framework, with support for stubbing and mocking


%prep

%build

%install
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

# remove vcs files
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore
%files
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
#% doc % {ruby_gemdir}/gems/% {oname}-% {version}/History.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/License.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.md
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.8.0-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.8.0-1
+ Revision: 767042
- version update 2.8.0

* Sat Sep 10 2011 Alexander Barakin <abarakin@mandriva.org> 2.6.0-3
+ Revision: 699182
- after bootstrap

  + Andrey Smirnov <asmirnov@mandriva.org>
    - bump release
    - remove rspec-core from reqs

* Thu Sep 08 2011 Andrey Smirnov <asmirnov@mandriva.org> 2.6.0-1
+ Revision: 699021
- missing rdoc fix
- rpmlint warning
- imported package rubygem-rspec-mocks

* Wed Dec 01 2010 Rémy Clouard <shikamaru@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 604555
- import rubygem-rspec-mocks

