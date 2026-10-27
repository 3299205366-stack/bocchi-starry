"""Local static server with byte ranges for media seeking."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re, os, argparse
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*a,**kw): super().__init__(*a,directory=str(Path(__file__).parent/'dist'),**kw)
    def send_head(self):
        self.remaining=None
        path=self.translate_path(self.path)
        value=self.headers.get('Range')
        if not value or not os.path.isfile(path): return super().send_head()
        size=os.path.getsize(path); match=re.fullmatch(r'bytes=(\d*)-(\d*)',value)
        if not match or not any(match.groups()): self.send_error(416);return None
        a,b=match.groups();start=int(a) if a else max(0,size-int(b));end=min(int(b),size-1) if a and b else size-1
        if start>end or start>=size:
            self.send_response(416);self.send_header('Content-Range',f'bytes */{size}');self.end_headers();return None
        stream=open(path,'rb');stream.seek(start);self.remaining=end-start+1
        self.send_response(206);self.send_header('Content-Type',self.guess_type(path));self.send_header('Content-Length',str(self.remaining));self.send_header('Content-Range',f'bytes {start}-{end}/{size}');self.send_header('Accept-Ranges','bytes');self.end_headers();return stream
    def copyfile(self,source,target):
        if self.remaining is None:return super().copyfile(source,target)
        remaining=self.remaining
        while remaining:
            block=source.read(min(65536,remaining))
            if not block:break
            target.write(block);remaining-=len(block)
    def end_headers(self):
        self.send_header('Cache-Control','no-cache');super().end_headers()
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=5178);args=p.parse_args()
    print(f'STARRY: http://localhost:{args.port}/',flush=True)
    ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
