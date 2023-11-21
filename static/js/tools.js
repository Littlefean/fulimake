// 123123123


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // 判断cookie名称是否匹配
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

console.log(csrftoken, "###");

class sysFetch {
    constructor() {

    }

    /**
     * 仅供类内部调用
     * @param urlFix
     * @param sendJson
     * @param resFunc
     * @param method
     * @private
     */
    static _fetch(urlFix, resFunc, method, sendJson) {
        let _curResponse = '...';

        fetch(`http://localhost:8000/${urlFix}`, {
            method,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: method === "GET" ? null :JSON.stringify(sendJson),
        }).then(response => {
            _curResponse = response;
            console.log(typeof _curResponse, _curResponse);
            return response.json()
        }).then(data => {
            // 处理响应数据
            resFunc(data);
        }).catch(error => {
            // 处理错误
            if (error instanceof SyntaxError) {
                // response是html字符串，将html字符串显示到界面上
                console.log(_curResponse, typeof _curResponse);
            }
            console.error("Error:", error);
        });
    }

    static get(urlFix, resFunc) {
        this._fetch(urlFix, resFunc, "GET", {});
    }

    static post(urlFix, sendJson, resFunc) {
        this._fetch(urlFix, resFunc, "POST", sendJson);
    }

    static put(urlFix, sendJson, resFunc) {
        this._fetch(urlFix, resFunc, "PUT", sendJson);
    }

    static delete(urlFix, resFunc) {
        this._fetch(urlFix, resFunc, "DELETE", {});
    }
}