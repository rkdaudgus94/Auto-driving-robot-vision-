#include <boost/asio.hpp>

using namespace::boost::asio;

int main()
{
    io_service io;
    serial_port sp(io, "/dev/ttyUSB0");  // 시리얼 포트를 open합니다. 여기서 "/dev/ttyUSB0"는 라즈베리파이에서 젯슨나노로 연결된 USB 포트 이름을 넣어야 합니다.
    
    sp.set_option(serial_port_base::baud_rate(9600)); // baud rate를 설정합니다. 여기서는 예시로 9600을 사용했습니다.

    // 쓰기
    std::string data = "Hello World!";
    write(sp, buffer(data));

    // 읽기
    char buf[128];
    read(sp, buffer(buf));
    std::cout << buf << std::endl;

    return 0;
}
