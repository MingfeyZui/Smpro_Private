import argparse     #是python的一个命令行解析包，非常编写可读性非常好的程序
import sys

from hw4.mingfei.text_vectors import DocumentCollection,SearchEngine

def main(argv):                                          # in diese Funciton wird sys.arg aufgerufen
    parser = argparse.ArgumentParser()                    #命令解析
    parser.add_argument('-d', '--dir', required =True)    #python interactive_search.py -dir ordenerName
    opts = parser.parse_args(argv)                          # 命令机械使用
    doc_collection = DocumentCollection.from_dir(opts.dir, ".txt")
    searcher = (doc_collection)     #在docs 中搜索
    while True:
        query_str = input("Query: ").strip()     #输入query
        if not query_str:
            break
        top_docs = searcher.ranked_documents(query_str)
        print("Results: %d" % len(top_docs))       # "Result: " + len(top_docs)
        for doc, sim in top_docs[:3]:
            print("%.4f %s" % (sim, doc.id))
            for snippet in searcher.snippets(query_str, doc):
                print("  %s" % snippet)
        print()


if __name__ == "__main__":          # module loader, um die function des name entsprended auszuführen ,hier Function name : main, so in the String ist es _main_
    main(sys.argv[1:])
