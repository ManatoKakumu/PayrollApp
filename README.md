アルバイト先の個別指導塾の給与計算アプリを作ってみました。 アルバイト先での給与計算は、働いた日は業務報告用紙に実施業務（業務時間）を記入し、月末に電卓を使って給与を計算していたため、給与計算に時間がかかっていました。 そこで、給与計算を簡単なGUI処理のみで自動的に給与計算を行い、時間短縮させることと、ペーパーレスを目的にこのアプリを構築しました。

開発環境はDjango、バージョン4.1です。 1.Djangoをインストール 2.「manage.py」があるディレクトリまで移動 3.「python manage.py runserver」コマンドでローカルサーバーにWebアプリが立ち上がります 4.「http://127.0.0.1:8000/」 をGoogle Chrome等に入力します。 5.アプリの画面が表示されます。

各ブランチの説明

first_version : 給与計算、勤怠報告、講師情報登録、授業情報登録が行えます。また、アルバイト先の塾では、同じ曜日は基本的に勤務内容が同じなので、授業情報登録さえ行えば（最悪、授業情報登録は行わなくても大丈夫です）、勤怠報告において入力するべき内容が自動で入力されるようになっているため、楽に勤怠報告を行えます。※いつもと違う業務内容だった場合は、その部分だけは手動で入力する必要があります。
給与計算は従来、電卓を叩いて行っていましたが、簡単なGUI操作のみで給与を計算・表示するため、勤怠報告と給与計算にかかる時間／勤怠報告に使用していた紙を削減することができます。

second_version : first_versionに冗長なコードが多かったため、リファクタリングしたものになります。機能はfirst_versionと変わりません。また、first_versionでは実現したい機能を実装することを目的としていたため、views.pyにおいてclassと関数がどちらもありましたが、second_versionにてclassベースのものに変更しました。

new_version : second_versionよりもより業務を効率化するための新たな機能の実装に取り組んでいます。まずは、1か月の業務内容をCSV出力することに取り組みます。
