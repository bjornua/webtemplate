<%inherit file="/html5.mako"/>
<head>
    <title>Unavngivet hjemmeside</title>
    <link rel="stylesheet" type="text/css" href="/static/css/main.css" />
</head>
<body>
    <div id="page">
        <div id="header">
            <h1>Unavngivet hjemmeside</h1>
        </div>
        <hr/>
        <ul>
            <li><a href="${urlfor("index")}">Forside</a></li>
            <li><a href="javascript:void();">Menulink 1</a></li>
            <li><a href="javascript:void();">Menulink 2</a></li>
            <li><a href="javascript:void();">Menulink 3</a></li>
            <li><a href="javascript:void();">Menulink 4</a></li>
            <li><a href="javascript:void();">Menulink 5</a></li>
        </ul>
        <hr/>
        ${next.body()}
    </div>
</body>
