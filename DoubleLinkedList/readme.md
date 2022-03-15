

<body>
<h1>Zweifach verkettete Liste</h1>

<p>Ein Projekt mit der man eine zweifach verkettete Liste, als auch eine Arraylist erstellen kann.
Folgende Funktionen werden angeboten:<br>
Element am Ende hinzufügen<br>
Länge der Liste ausgeben<br>
Alle Elemente der Liste ausgeben<br>
Element vor einem anderen Element (nach index) einfügen <br>
Element nach einem anderen Element (nach index) einfügen <br>
Element vor einem anderen Element (nach index) löschen <br>
Element nach einem anderen Element (nach index) löschen <br>
Größtes Element ausgeben <br>
Kleinstes Element ausgeben <br>
Ein bestimmtes Element suchen -> Ausgabe: Stelle des Elements <br>
Absteigend sortieren </br>
Aufsteigend sortieren </br>
</p>

<p>Als Beispiel wurden in jeder Datenstruktur 10000 Zufallszahlen von 0-10000 eingefügt. Anschließend wurden diese mit den angebotenen Methoden sortiert. Die Arraylist braucht durchschnittlich ca. zweimal solange wie die Double Linked List -> Double Linked List ca. 3-4 sek, Arraylist ca. 6-8 sek.</p>


  <h2>Aufwandsklassen</h2>
<table>
  <tr>
    <th>Methode</th>
    <th>DoubleLinkedList</th>
    <th>ArrayList</th>
  </tr>
  <tr>
    <td>getLength</td>
    <td>n</td>
    <td>n</td>
  </tr>
  <tr>
    <td>printAll</td>
    <td>n</td>
    <td>n</td>
  </tr>
  <tr>
    <td>append</td>
    <td>n</td>
    <td>1</td>
  </tr>
  <tr>
    <td>InsertAfterIndex</td>
    <td>n</td>
    <td>n</td>
  </tr>
  <tr>
    <td>InsertAfterNode</td>
    <td>1</td>
    <td>---</td>
  </tr>
    <tr>
    <td>InsertBeforeIndex</td>
    <td>n</td>
    <td>n</td>
  </tr>
    <tr>
    <td>InsertBeforeNode</td>
    <td>1</td>
    <td>---</td>
  </tr>
    <tr>
    <td>DelteAfterIndex</td>
    <td>n</td>
    <td>n</td>
  </tr>
  <tr>
    <td>DeleteAfterNode</td>
    <td>1</td>
    <td>---</td>
  </tr>
    <tr>
    <td>DeleteBeforeIndex</td>
    <td>n</td>
    <td>n</td>
  </tr>
    <tr>
    <td>DeleteBeforeNode</td>
    <td>1</td>
    <td>---</td>
  </tr>
      <tr>
    <td>getMax</td>
    <td>n</td>
    <td>n</td>
  </tr>
  <tr>
    <td>getMin</td>
    <td>n</td>
    <td>n</td>
  </tr>
  <tr>
    <td>sortAsc</td>
    <td>n^2</td>
    <td>n^2</td>
  </tr>
  <tr>
    <td>sortDesc</td>
    <td>n^2</td>
    <td>n^2</td>
  </tr>
</table>
</body>
