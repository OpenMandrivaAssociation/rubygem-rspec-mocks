%define oname rspec-mocks
%define geminstdir %{ruby_gemdir}/gems/%{oname}-%{version}

Summary:    Behaviour Driven Development for Ruby
Name:       rubygem-%{oname}
Version:    2.0.1
Release:    %mkrel 1
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/rspec/rspec-mocks
Source0:    %{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(rspec-core) = %{version}
Requires:   rubygem(rspec-expectations) = %{version}
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
RSpec's 'test double' framework, with support for stubbing and mocking


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

# remove vcs files
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore
%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.autotest
%{ruby_gemdir}/gems/%{oname}-%{version}/.document
%{ruby_gemdir}/gems/%{oname}-%{version}/cucumber.yml
%{ruby_gemdir}/gems/%{oname}-%{version}/Gemfile
%{ruby_gemdir}/gems/%{oname}-%{version}/autotest/
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.markdown
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/License.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.markdown
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/specs.watchr
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
