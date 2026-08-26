#ifndef MAINMENU_H
#define MAINMENU_H

#include <QWidget>
class MainWindow;

class MainMenu : public QWidget
{
    Q_OBJECT
public:
    explicit MainMenu(MainWindow *parent = nullptr);

private:
    MainWindow *mainWindow;
};

#endif // MAINMENU_H
