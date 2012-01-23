%define oname rspec-mocks
%define geminstdir %{ruby_gemdir}/gems/%{oname}-%{version}

Summary:    Behaviour Driven Development for Ruby
Name:       rubygem-%{oname}
Version:    2.8.0
Release:    1
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
