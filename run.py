from src.api.manage import app

if __name__ == '__main__':
    status = False
    app.run(debug=True, host='0.0.0.0', port=5555)   