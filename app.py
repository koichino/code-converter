from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_type = "azure"
openai.api_base = "https://<OpenAIリソース名>.openai.azure.com/"
# ChatGPT 以外の場合
#openai.api_version = "2022-12-01"
#ChatGPTの場合
openai.api_version = "2023-03-15-preview"
openai.api_key = "<API Key>"



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def translate():
    if request.method == "POST":
        source_language = request.form.get("source")
        target_language = request.form.get("target")
        code = request.form.get("code")

        #systemPrompt = f"あなたはソースコードを他の言語に変換するプロです。英語以外の文字は日本語だと思ってください。コメントもそのまま日本語に変換します。"
        prompt = f"""
        ###指示
        あなたはソースコードを他の言語に変換するプロです。英語以外の文字は日本語です。コメントも日本語で出力します。
        回答はソースコードのみを返すようにします。回答へはChatMLのタグ（<|im_end|>など）を除去してください。
        コード変換をお願いします from {source_language} into {target_language}
        ### {source_language}
        {code} 
        ### {target_language} 
        """

        #msg = [{"role":"system","content":systemPrompt},{"role":"user","content":prompt},{"role":"assistant","content":""}]
        #print(msg)

        response = openai.Completion.create(
#            engine="code-davinci-002",
            engine="gpt35-0301",
            #messages = [
            #    {"role":"system","content":""},
            #    {"role":"user","content":"ChatGPTについて教えてください"}
            #    ], #ChatGPTの場合使用
            prompt=prompt,
            temperature=0,
            max_tokens=1050,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["###"]
        )

        print(response)

        output = response.choices[0].text

        # 文字列の各行の先頭のスペースを文字の出現まで削除する
        output = os.linesep.join([s.lstrip() for s in output.splitlines()])

        print(output)
        return render_template("translate.html", output=output)
#        return render_template("index.html", output=output)


if __name__ == '__main__':
    app.run()
