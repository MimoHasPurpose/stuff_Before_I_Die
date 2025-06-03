import gradio as gr

def greet(name,surname):
    return "Hello "+name+"!"+surname

demo=gr.Interface(
    fn=greet,
    inputs=["text","text"],
    outputs=["text","text"],
)
demo.launch(share =True)