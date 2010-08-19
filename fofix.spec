%define name fofix
%define version 3.121
%define release %mkrel 1

Summary: 	FoFiX - A fork of FretsOnFire
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Group:   	Games/Arcade
License: 	GPL
URL:     	http://code.google.com/p/fofix/
Source:  	%{name}-%{version}.tar.bz2
BuildRequires:  desktop-file-utils
BuildArch:      noarch 
BuildRoot: 	%{_tmppath}/%{name}-%{version}-build
Requires:       python >= 2.5
Requires:       python-numpy
Requires:       python-imaging
Requires:       python-opengl
Requires:       pygame
Requires:	pyvorbis
Requires:	python-pyxml



%description
FretsOnFire fork with plenty of features, customizable themes and options
A multi-OS rhythm game, written in Python, similar to Guitar Hero or Rock Band. Play guitar, 
bass or drums along with your favorite songs on your computer using either your keyboard or 
instruments. You can use your Guitar Hero or Rock Band instrument controllers.

Separated audio tracks will mute when you fail to hit or sustain the required notes correctly 
to simulate a real concert-playing experience.
Simplified list of features

    * Completely Customizable Graphics (standard .PNG format)
    * Completely Customizable Sound Effects & Menu Music (standard .OGG format)
    * Completely Customizable Fretboard Point Of View (POV)
    * Completely Customizable Menus and Layouts
    * 2D or 3D Notes & Frets
    * 3D Note Texturing
    * Unlimited Themes
    * Unlimited Necks
    * Graphical Neck Selection
    * Multiplayer Support with several different game types (2 players only for now, battle and cooperative modes)
    * Random Stages, Stage Rotation (slideshow) and basic Animated Stages
    * Support for seperated song, guitar, bass and drum audio tracks
    * Guitar playable & separated track support
    * Lead Guitar & Rhythm Guitar playable track support
    * Bass Guitar playable & separated track support
    * Bass Groove 5x, 6x, 10x, and 12x multiplier support
    * Drums playable & separated track support
    * Starpower/Overdrive
    * Big Rock Endings
    * Drum Fills to activate starpower / overdrive
    * Native MIDI instrument input / controller support
    * Pitch-bending whammy DSP effect
    * Songlist metadata caching for faster subsequent load times
    * Both digital and analog Killswitch effects (Pseudo whammy bar support)
    * Jurgen (Computer Player, skilled at guitar / bass / drums)
    * Support for Guitar Solos, Bass Solos, and Drum Solos
    * Practice mode: single-track, full-speed, selectable start position / section
    * Slowdown mode: single or multiple tracks, 3/4, 1/2 or 1/4 speed (for now)
    * Tutorial songs (4 so far)
    * Customizable HO/POs (including chord pull-offs) and Note Hit Window
    * In-Game Status Display
    * In-Game Star Score Display (continuous partial star fillup available)
    * Optional scrolling or static MIDI / RockBand lyrics (where available)
    * World high score chart with optional score uploading 

%prep
%setup -q 


%build

%install
export DONT_STRIP=1
rm -rf %{buildroot}
# launcher
mkdir -p %buildroot%_bindir/
cat > %buildroot%_bindir/%{name} << EOF
#!/bin/sh
cd %{_datadir}/games/%{name}/src
%__python ./FoFiX.py "\$@"
EOF

chmod +x %{buildroot}%{_bindir}/%{name}

%__install -dm 755 %{buildroot}%{_datadir}/games/%{name}
%__cp -a data \
	%{buildroot}%{_datadir}/games/%{name}
%__cp -a src \
	%{buildroot}%{_datadir}/games/%{name}

# icon
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 data/mfhlogo.png \
	%{buildroot}%{_datadir}/pixmaps/%{name}.png

#Menu entry
install -d -m755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=FoFix
Comment=Game of Musical Skill and Fast Fingers
Exec=%{name}
Icon=%{_datadir}/pixmaps/%{name}.png
Terminal=false
Type=Application
Categories=Game;X-MandrivaLinux-MoreApplications-Games-Arcade;Games-Arcade
EOF


%clean
rm -rf %{buildroot}

%post
%{update_desktop_database}


%postun
%{clean_desktop_database}

%files 
%defattr(-, root, root)
%doc COPYING CREDITS AUTHORS
%doc doc/*
%_bindir/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/games/%{name}

