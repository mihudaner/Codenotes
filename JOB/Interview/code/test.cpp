
#include <atomic>
#include "mingw.thread.h"
#include <iostream>
#include <sstream>
using namespace std;
enum type
{
    Txt,
    Picture,
    Video,
};

class ISplitter
{

};
class TxtSplitter: public ISplitter {

};

class PictureSplitter: public ISplitter {

};

class VideoSplitter: public ISplitter {

};

class Factory
{
    ISplitter* getsplit(type type)
    {
        switch(type)
        {
            case Txt:
                return new TxtSplitter();
            case Picture:
                return new TxtSplitter();
            case Video:
                return new TxtSplitter();
            default:
                return nullptr;
        }
    }
};

