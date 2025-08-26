import os
import glob

def merge_and_filter_text_files(input_pattern, output_file, filter_char='@'):
    """
    读取多个文本文件，过滤掉包含特定字符的行，并合并到一个输出文件中
    
    参数:
        input_pattern (str): 输入文件的匹配模式（例如：*.txt 或 file*.txt）
        output_file (str): 输出文件的路径和名称
        filter_char (str): 要过滤的字符，默认是'@'
    """
    try:
        # 获取匹配模式的所有文件
        file_list = glob.glob(input_pattern)
        
        if not file_list:
            print(f"没有找到匹配模式 '{input_pattern}' 的文件")
            return
        
        print(f"找到 {len(file_list)} 个文件:")
        for file in file_list:
            print(f"  - {file}")
        
        # 按文件名排序（可选）
        file_list.sort()
        
        # 统计信息
        total_lines = 0
        filtered_lines = 0
        
        # 打开输出文件
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write('#EXTM3U x-tvg-url="https://baoer.org.cn/e.xml" catchup="append" catchup-days="5" catchup-source="?playseek={utc:YmdHMS}-{utcend:YmdHMS}"')
            outfile.write(f"\n")
            # 遍历所有文件
            for filename in file_list:
                try:
                    # 读取文件内容并过滤
                    with open(filename, 'r', encoding='utf-8') as infile:
                        file_lines = 0
                        file_filtered = 0
                        
                        for line in infile:
                            total_lines += 1
                            file_lines += 1
                            
                            # 检查是否包含过滤字符
                            if filter_char in line:
                                filtered_lines += 1
                                file_filtered += 1
                                continue  # 跳过包含过滤字符的行
                            
                            # 写入过滤后的行
                            outfile.write(line)
                    
                    print(f"已处理: {filename} (共 {file_lines} 行，过滤 {file_filtered} 行)")
                    
                except Exception as e:
                    print(f"处理文件 {filename} 时出错: {str(e)}")
        
        # 输出统计信息
        print(f"\n处理完成!")
        print(f"总共处理了 {total_lines} 行")
        print(f"过滤掉了 {filtered_lines} 行")
        print(f"合并后的文件保存为: {output_file}")
        
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    # 设置输入文件模式（可以根据需要修改）
    input_pattern = "./TV-List/*.txt"  # 合并当前目录下所有txt文件
    
    # 设置输出文件路径（可以根据需要修改）
    output_file = "yu.m3u"
    
    # 设置要过滤的字符（可以根据需要修改）
    filter_char = "# "  # 过滤包含# 符号的行
    
    # 执行合并和过滤
    merge_and_filter_text_files(input_pattern, output_file, filter_char)