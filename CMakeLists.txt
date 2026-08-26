cmake_minimum_required(VERSION 3.5)

project(Fase1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Widgets)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Widgets)

set(PROJECT_SOURCES
    main.cpp
    mainwindow.cpp
    mainwindow.h
    matematica/LogicaMatematica.cpp
    matematica/LogicaMatematica.h
    pantallas/MainMenu.cpp
    pantallas/MainMenu.h
    pantallas/PermutacionCombinacion.cpp
    pantallas/PermutacionCombinacion.h
    pantallas/ProductoCartesiano.cpp
    pantallas/ProductoCartesiano.h
    pantallas/DiagramaVenn.cpp
    pantallas/DiagramaVenn.h
    pantallas/Resultados.cpp
    pantallas/Resultados.h
)

if(${QT_VERSION_MAJOR} GREATER_EQUAL 6)
    qt_add_executable(Fase1
        MANUAL_FINALIZATION
        ${PROJECT_SOURCES}
    )
else()
    add_executable(Fase1
        ${PROJECT_SOURCES}
    )
endif()

target_link_libraries(Fase1 PRIVATE Qt${QT_VERSION_MAJOR}::Widgets)

if(APPLE)
    set_target_properties(Fase1 PROPERTIES
        MACOSX_BUNDLE TRUE
        MACOSX_BUNDLE_GUI_IDENTIFIER my.domain.Fase1
        MACOSX_BUNDLE_BUNDLE_VERSION "1.0"
        MACOSX_BUNDLE_SHORT_VERSION_STRING "1.0"
    )
endif()

if(QT_VERSION_MAJOR EQUAL 6)
    qt_finalize_executable(Fase1)
endif()
