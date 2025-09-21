#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
端口掃描程式
掃描指定主機的所有端口，查看哪些端口是開啟的
"""

import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys

class PortScanner:
    def __init__(self, host, timeout=1):
        """
        初始化端口掃描器
        
        Args:
            host (str): 要掃描的主機地址
            timeout (int): 連接超時時間（秒）
        """
        self.host = host
        self.timeout = timeout
        self.open_ports = []
        self.lock = threading.Lock()
    
    def scan_port(self, port):
        """
        掃描單個端口
        
        Args:
            port (int): 要掃描的端口號
            
        Returns:
            tuple: (port, is_open, service_name)
        """
        try:
            # 創建 socket 連接
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            # 嘗試連接
            result = sock.connect_ex((self.host, port))
            sock.close()
            
            if result == 0:
                # 端口開啟，嘗試獲取服務名稱
                service_name = self.get_service_name(port)
                return (port, True, service_name)
            else:
                return (port, False, None)
                
        except Exception as e:
            return (port, False, f"錯誤: {str(e)}")
    
    def get_service_name(self, port):
        """
        獲取端口對應的服務名稱
        
        Args:
            port (int): 端口號
            
        Returns:
            str: 服務名稱
        """
        try:
            service_name = socket.getservbyport(port)
            return service_name
        except OSError:
            # 如果無法獲取服務名稱，返回常見端口的描述
            common_ports = {
                21: "FTP",
                22: "SSH",
                23: "Telnet",
                25: "SMTP",
                53: "DNS",
                80: "HTTP",
                110: "POP3",
                143: "IMAP",
                443: "HTTPS",
                993: "IMAPS",
                995: "POP3S",
                3389: "RDP",
                5432: "PostgreSQL",
                3306: "MySQL",
                6379: "Redis",
                27017: "MongoDB"
            }
            return common_ports.get(port, "未知服務")
    
    def scan_range(self, start_port=1, end_port=65535, max_threads=100):
        """
        掃描端口範圍
        
        Args:
            start_port (int): 起始端口
            end_port (int): 結束端口
            max_threads (int): 最大線程數
        """
        print(f"開始掃描 {self.host} 的端口 {start_port}-{end_port}")
        print(f"使用 {max_threads} 個線程，超時時間: {self.timeout} 秒")
        print("-" * 60)
        
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            # 提交所有掃描任務
            future_to_port = {
                executor.submit(self.scan_port, port): port 
                for port in range(start_port, end_port + 1)
            }
            
            # 處理完成的任務
            for future in as_completed(future_to_port):
                port, is_open, service_name = future.result()
                
                if is_open:
                    with self.lock:
                        self.open_ports.append((port, service_name))
                        print(f"✓ 端口 {port:5d} 開啟 - {service_name}")
        
        end_time = time.time()
        scan_time = end_time - start_time
        
        print("-" * 60)
        print(f"掃描完成！耗時: {scan_time:.2f} 秒")
        print(f"發現 {len(self.open_ports)} 個開啟的端口")
        
        if self.open_ports:
            print("\n開啟的端口列表:")
            print("端口號    服務名稱")
            print("-" * 30)
            for port, service in sorted(self.open_ports):
                print(f"{port:5d}    {service}")
        else:
            print("沒有發現任何開啟的端口")

def main():
    """主程式"""
    # 目標主機
    target_host = "nat3.turbotech.com.tw"
    target_host = "ithelp.ithome.com.tw"
    target_host = "ojt.wda.gov.tw"
    target_host = "cms.motc.got.tw"
    target_host = "ojtims.wda.gov.tw"
    
    print("=" * 60)
    print("端口掃描程式")
    print("=" * 60)
    print(f"目標主機: {target_host}")
    
    # 創建掃描器實例
    scanner = PortScanner(target_host, timeout=1)
    
    try:
        # 掃描常用端口範圍 (1-1000)
        print("\n第一階段: 掃描常用端口 (1-1000)")
        scanner.timeout=2
        scanner.scan_range(1, 1000, max_threads=500)
        
        # 如果發現開啟的端口，繼續掃描完整範圍
        if scanner.open_ports:
            print(f"\n發現 {len(scanner.open_ports)} 個開啟的端口，繼續掃描完整範圍...")
            scanner.open_ports = []  # 重置列表
            scanner.timeout=2
            scannerportmax=25535 # 65535
            scanner.scan_range(1, scannerportmax, max_threads=3000)
        
    except KeyboardInterrupt:
        print("\n\n掃描被用戶中斷")
    except Exception as e:
        print(f"\n掃描過程中發生錯誤: {str(e)}")
    
    print("\n程式結束")

if __name__ == "__main__":
    main()
