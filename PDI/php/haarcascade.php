<?php
$postdata = file_get_contents("php://input");
$request = json_decode($postdata);
$name = $request->name;
$qtd = $request->qtd;
$v1 = $request->v1;
$v2 = $request->v2;
$qtda = $qtd - 1;

$local2 = 'python C:\xampp\htdocs\PDI\python\\'.$name.'.py C:\xampp\htdocs\PDI\images\img'.$qtda.'.png '.$v1.' '.$v2.' C:\xampp\htdocs\PDI\images\img'.$qtd.'.png';
$local = 'C:\WINDOWS\system32\cmd.exe /c START C:\xampp\htdocs\PDI\exec.bat '.$local2;
passthru($local);

