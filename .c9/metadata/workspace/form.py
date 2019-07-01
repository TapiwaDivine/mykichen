{"filter":false,"title":"form.py","tooltip":"/form.py","undoManager":{"mark":66,"position":66,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":33},"action":"insert","lines":["from flask import Flask","from flask_wtf import FlaskForm","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo","","class RegistrationForm(FlaskForm):","    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=25)])","    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])","    submit = SubmitField('Sign Up')","    ","class LoginForm(FlaskForm):","    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=25)])","    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])","    remember_me = BooleanField ('Remember Me')","    submit = SubmitField('Login')"],"id":1}],[{"start":{"row":5,"column":34},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["f"],"id":3},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["i"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["t"],"id":4},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"remove","lines":["s"],"id":5},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"remove","lines":["t"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"remove","lines":["r"]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["r"],"id":6},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["s"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["_"],"id":7},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["n"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["a"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["m"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":[" "],"id":8},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["="]}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":[" "],"id":9},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["S"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["t"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["i"],"id":10}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":21},"action":"remove","lines":["Stri"],"id":11},{"start":{"row":6,"column":17},"end":{"row":6,"column":28},"action":"insert","lines":["StringField"]}],[{"start":{"row":6,"column":28},"end":{"row":6,"column":30},"action":"insert","lines":["()"],"id":12}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":31},"action":"insert","lines":["''"],"id":13}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["F"],"id":14},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["i"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["s"],"id":15},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":[" "],"id":16},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["N"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["a"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["m"]}],[{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["e"],"id":17}],[{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"insert","lines":[","],"id":18}],[{"start":{"row":6,"column":43},"end":{"row":6,"column":69},"action":"insert","lines":["validators=[DataRequired()"],"id":19}],[{"start":{"row":6,"column":68},"end":{"row":6,"column":69},"action":"remove","lines":[")"],"id":20},{"start":{"row":6,"column":67},"end":{"row":6,"column":68},"action":"remove","lines":["("]},{"start":{"row":6,"column":66},"end":{"row":6,"column":67},"action":"remove","lines":["d"]},{"start":{"row":6,"column":65},"end":{"row":6,"column":66},"action":"remove","lines":["e"]},{"start":{"row":6,"column":64},"end":{"row":6,"column":65},"action":"remove","lines":["r"]},{"start":{"row":6,"column":63},"end":{"row":6,"column":64},"action":"remove","lines":["i"]},{"start":{"row":6,"column":62},"end":{"row":6,"column":63},"action":"remove","lines":["u"]},{"start":{"row":6,"column":61},"end":{"row":6,"column":62},"action":"remove","lines":["q"]},{"start":{"row":6,"column":60},"end":{"row":6,"column":61},"action":"remove","lines":["e"]},{"start":{"row":6,"column":59},"end":{"row":6,"column":60},"action":"remove","lines":["R"]},{"start":{"row":6,"column":58},"end":{"row":6,"column":59},"action":"remove","lines":["a"]},{"start":{"row":6,"column":57},"end":{"row":6,"column":58},"action":"remove","lines":["t"]},{"start":{"row":6,"column":56},"end":{"row":6,"column":57},"action":"remove","lines":["a"]},{"start":{"row":6,"column":55},"end":{"row":6,"column":56},"action":"remove","lines":["D"]},{"start":{"row":6,"column":54},"end":{"row":6,"column":55},"action":"remove","lines":["["]},{"start":{"row":6,"column":53},"end":{"row":6,"column":54},"action":"remove","lines":["="]},{"start":{"row":6,"column":52},"end":{"row":6,"column":53},"action":"remove","lines":["s"]},{"start":{"row":6,"column":51},"end":{"row":6,"column":52},"action":"remove","lines":["r"]},{"start":{"row":6,"column":50},"end":{"row":6,"column":51},"action":"remove","lines":["o"]},{"start":{"row":6,"column":49},"end":{"row":6,"column":50},"action":"remove","lines":["t"]},{"start":{"row":6,"column":48},"end":{"row":6,"column":49},"action":"remove","lines":["a"]},{"start":{"row":6,"column":47},"end":{"row":6,"column":48},"action":"remove","lines":["d"]},{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"remove","lines":["i"]},{"start":{"row":6,"column":45},"end":{"row":6,"column":46},"action":"remove","lines":["l"]},{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"remove","lines":["a"]},{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"remove","lines":["v"]},{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"remove","lines":[","]},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"remove","lines":[")"]}],[{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":[")"],"id":21}],[{"start":{"row":6,"column":42},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["l"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["a"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["s"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["I"],"id":23},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["n"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["a"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["m"]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"remove","lines":["e"],"id":24},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"remove","lines":["m"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"remove","lines":["a"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"remove","lines":["n"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"remove","lines":["I"]}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["_"],"id":25},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["n"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["a"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["m"]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":[" "],"id":26},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":[" "],"id":27},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["S"]},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["t"]},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["r"]}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":19},"action":"remove","lines":["Str"],"id":28},{"start":{"row":7,"column":16},"end":{"row":7,"column":27},"action":"insert","lines":["StringField"]}],[{"start":{"row":7,"column":27},"end":{"row":7,"column":29},"action":"insert","lines":["()"],"id":29}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":30},"action":"insert","lines":["''"],"id":30}],[{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["L"],"id":31},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["a"]},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["s"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":[" "],"id":32},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["N"]},{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["a"]},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["m"]},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":40},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":33},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "],"id":34},{"start":{"row":7,"column":40},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":8,"column":90},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["e"],"id":36},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["m"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["a"]}],[{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["i"],"id":37},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["l"]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":[" "],"id":38},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":[" "],"id":39},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["S"]}],[{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["t"],"id":40}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":14},"action":"remove","lines":["St"],"id":41},{"start":{"row":9,"column":12},"end":{"row":9,"column":23},"action":"insert","lines":["StringField"]}],[{"start":{"row":9,"column":23},"end":{"row":9,"column":25},"action":"insert","lines":["()"],"id":42}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":26},"action":"insert","lines":["''"],"id":43}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["E"],"id":44},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["m"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["a"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["i"]},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["l"]}],[{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"insert","lines":[","],"id":45}],[{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"insert","lines":[" "],"id":46}],[{"start":{"row":9,"column":34},"end":{"row":9,"column":85},"action":"insert","lines":["validators=[DataRequired(), Length(min=2, max=25)])"],"id":47}],[{"start":{"row":9,"column":61},"end":{"row":9,"column":85},"action":"remove","lines":[" Length(min=2, max=25)])"],"id":48},{"start":{"row":9,"column":60},"end":{"row":9,"column":61},"action":"remove","lines":[","]}],[{"start":{"row":9,"column":60},"end":{"row":9,"column":61},"action":"insert","lines":["}"],"id":49}],[{"start":{"row":9,"column":60},"end":{"row":9,"column":61},"action":"remove","lines":["}"],"id":50}],[{"start":{"row":9,"column":60},"end":{"row":9,"column":61},"action":"insert","lines":["]"],"id":51}],[{"start":{"row":10,"column":92},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":52},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":92},"action":"insert","lines":["password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])"],"id":53}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["c"],"id":54},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["o"]}],[{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":["n"],"id":55}],[{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["f"],"id":56},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["r"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["i"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["m"]}],[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"remove","lines":["m"],"id":57},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"remove","lines":["i"]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"remove","lines":["r"]}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["i"],"id":58},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["r"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["n"]}],[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"remove","lines":["n"],"id":59}],[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["m"],"id":60},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["_"]}],[{"start":{"row":11,"column":38},"end":{"row":11,"column":39},"action":"insert","lines":["C"],"id":61},{"start":{"row":11,"column":39},"end":{"row":11,"column":40},"action":"insert","lines":["o"]},{"start":{"row":11,"column":40},"end":{"row":11,"column":41},"action":"insert","lines":["n"]},{"start":{"row":11,"column":41},"end":{"row":11,"column":42},"action":"insert","lines":["f"]},{"start":{"row":11,"column":42},"end":{"row":11,"column":43},"action":"insert","lines":["r"]},{"start":{"row":11,"column":43},"end":{"row":11,"column":44},"action":"insert","lines":["i"]},{"start":{"row":11,"column":44},"end":{"row":11,"column":45},"action":"insert","lines":["m"]}],[{"start":{"row":11,"column":44},"end":{"row":11,"column":45},"action":"remove","lines":["m"],"id":62},{"start":{"row":11,"column":43},"end":{"row":11,"column":44},"action":"remove","lines":["i"]},{"start":{"row":11,"column":42},"end":{"row":11,"column":43},"action":"remove","lines":["r"]}],[{"start":{"row":11,"column":42},"end":{"row":11,"column":43},"action":"insert","lines":["i"],"id":63},{"start":{"row":11,"column":43},"end":{"row":11,"column":44},"action":"insert","lines":["r"]},{"start":{"row":11,"column":44},"end":{"row":11,"column":45},"action":"insert","lines":["m"]}],[{"start":{"row":11,"column":45},"end":{"row":11,"column":46},"action":"insert","lines":[" "],"id":64}],[{"start":{"row":9,"column":60},"end":{"row":9,"column":61},"action":"remove","lines":["]"],"id":65}],[{"start":{"row":9,"column":59},"end":{"row":9,"column":60},"action":"remove","lines":[")"],"id":66},{"start":{"row":9,"column":58},"end":{"row":9,"column":59},"action":"remove","lines":["("]},{"start":{"row":9,"column":57},"end":{"row":9,"column":58},"action":"remove","lines":["d"]},{"start":{"row":9,"column":56},"end":{"row":9,"column":57},"action":"remove","lines":["e"]},{"start":{"row":9,"column":55},"end":{"row":9,"column":56},"action":"remove","lines":["r"]},{"start":{"row":9,"column":54},"end":{"row":9,"column":55},"action":"remove","lines":["i"]},{"start":{"row":9,"column":53},"end":{"row":9,"column":54},"action":"remove","lines":["u"]},{"start":{"row":9,"column":52},"end":{"row":9,"column":53},"action":"remove","lines":["q"]}],[{"start":{"row":9,"column":51},"end":{"row":9,"column":52},"action":"remove","lines":["e"],"id":67},{"start":{"row":9,"column":50},"end":{"row":9,"column":51},"action":"remove","lines":["R"]},{"start":{"row":9,"column":49},"end":{"row":9,"column":50},"action":"remove","lines":["a"]},{"start":{"row":9,"column":48},"end":{"row":9,"column":49},"action":"remove","lines":["t"]},{"start":{"row":9,"column":47},"end":{"row":9,"column":48},"action":"remove","lines":["a"]},{"start":{"row":9,"column":46},"end":{"row":9,"column":47},"action":"remove","lines":["D"]},{"start":{"row":9,"column":45},"end":{"row":9,"column":46},"action":"remove","lines":["["]},{"start":{"row":9,"column":44},"end":{"row":9,"column":45},"action":"remove","lines":["="]},{"start":{"row":9,"column":43},"end":{"row":9,"column":44},"action":"remove","lines":["s"]},{"start":{"row":9,"column":42},"end":{"row":9,"column":43},"action":"remove","lines":["r"]},{"start":{"row":9,"column":41},"end":{"row":9,"column":42},"action":"remove","lines":["o"]},{"start":{"row":9,"column":40},"end":{"row":9,"column":41},"action":"remove","lines":["t"]},{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"remove","lines":["a"]},{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"remove","lines":["d"]},{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"remove","lines":["i"]},{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"remove","lines":["l"]},{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"remove","lines":["a"]},{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"remove","lines":["v"]},{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"remove","lines":[" "]},{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"remove","lines":[","]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":32},"end":{"row":9,"column":32},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1561330534365,"hash":"56672e86d13aee50705d34f88835fc5352685f97"}