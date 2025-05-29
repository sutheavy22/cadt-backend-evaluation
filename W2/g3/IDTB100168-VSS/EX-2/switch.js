const http = require('http');

const server = http.createServer((req, res) => {
    const url = req.url;
    const method = req.method;

    console.log(`Received ${method} request for ${url}`);


    if (method === 'GET') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });

        switch (url) {
            case '/':
                res.end('Welcome to the Home Page');
                break;
            case '/about':
                res.end('About us: at CADT, we love node.js!');
                break;
            case '/contact-us':
                res.end('You can reach us via email…');
                break;
            case '/products':
                res.end('Buy one get one…');
                break;
            case '/projects':
                res.end('Here are our awesome projects');
                break;
            default:
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end('404 Not Found');
        }

    } else {
        
        res.writeHead(405, { 'Content-Type': 'text/plain' });
        res.end(`Method ${method} Not Allowed`);
    }
});

server.listen(3000, () => {
    console.log('Server is running at http://localhost:3000');
});
