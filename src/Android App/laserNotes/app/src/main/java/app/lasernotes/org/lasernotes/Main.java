package app.lasernotes.org.lasernotes;

import android.graphics.Color;
import android.os.Bundle;
import android.os.StrictMode;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Main extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // E' necessario per effettuare connessioni di rete dal thread principale
        // Vedi: http://stackoverflow.com/questions/13136539/caused-by-android-os-networkonmainthreadexception
        if (android.os.Build.VERSION.SDK_INT > 9) {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }

        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        // Cambio il colore dell'icona e dello sfondo del bottone
        fab.setColorFilter(Color.WHITE);
        fab.setBackgroundTintList(getResources().getColorStateList(R.color.lnColor));

        /*
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
       */
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void ButtonProva_onClick(View v){
        TextView oText = (TextView) findViewById(R.id.textView);

        Client oClient = new Client("192.168.43.52",52000);

        /*
        * Cosa fa           :           Effettua il login comunicando con l'host
        * sUser             :           stringa, username per loggarsi
        * sPassword         :           stringa, md5(md5(della password))
        * Ritorna           :           sRet -> cookie generato dal server, oppure vuoto in caso di errore
        * */
        // String sRet = oClient.login("lucabertoni","b9be11166d72e9e3ae7fd407165e4bd2");

        /*
        *   Cosa fa             :               Registra un nuovo utente all'interno del server
        *   aUser               :               assocarray, array con i dati dell'utente, così formato:
        *                                           ["sNome"] => "Luca"
        *                                           ["sCognome"] => "Bertoni"
        *                                           ["sEmail"] => "luca.bertoni24@gmail.com"
        *                                           ["sUsername"] => "lucabertoni"
        *                                           ["sPassword"] => "b9be11166d72e9e3ae7fd407165e4bd2" (md5(md5("root")))
        *   Ritorna             :               bRet -> logico, true = Utente aggiunto | false = utente non aggiunto, errore
        *
        *   CLIENT: {'sComando': “addUser”, 'aUtente':{'sNome':'Luca',sCognome:'Bertoni','sEmail':'luca.bertoni24@gmail.com','sUsername':'lucabertoni','sPassword':'b9be11166d72e9e3ae7fd407165e4bd2','nLivello':1}}
        *   SERVER: {'sRisultato':'OK'} | {'sRisultato':'NO'}
        * */
        /*
        Map<String,String> aUser = new HashMap();
        aUser.put("sNome","Marco");
        aUser.put("sCognome","Bertoni");
        aUser.put("sEmail","marco@marco.it");
        aUser.put("sUsername", "marcobertoni");
        aUser.put("sPassword","b9be11166d72e9e3ae7fd407165e4bd2");
        boolean bRet = oClient.addUser(aUser);
        if(bRet){
            oText.setText("True!!");
        }else{
            oText.setText("False :(");
        }
        */

        /*
         *   Cosa fa            :               Estrapola il nome utente dello user
         *   sCookie            :               stringa, cookie associato all'utente
         *   Ritorna            :               sRet -> stringa, username dell'utente
         *
         *   CLIENT: {'sComando': “getUsername”, 'sCookie':”28c8edde3d61a041121511d3b1866f0636”}
         *   SERVER: {'sRisultato':'OK',”sUsername”:”lucabertoni”} | {'sRisultato':'NO'}
         * */
        /*
        String sUsername = oClient.getUsername("28c8edde3d61a041121511d3b1866f0636");
        oText.setText(sUsername);
        */

        /*
         *   Cosa fa            :               Estrae tutte le informazioni dell'utente
         *   sCookie            :               stringa, cookie associato all'utente
         *   Ritorna            :               aRet -> assocarray, dati dell'utente, così formato:
         *                                           ["sNome"]      => "Luca"
         *                                           ["sCognome"]   => "Bertoni"
         *                                           ["sEmail"]     => "luca.bertoni24@gmail.com"
         *                                           ["sUsername"]  => "lucabertoni"
         *                                           ["sPassword"]  => "b9be11166d72e9e3ae7fd407165e4bd2" (md5(md5("root")))
         *                                           ["nLivello"]   => "1"
         *
         *   CLIENT: {'sComando': “getAllUserInfo”, 'sCookie':”28c8edde3d61a041121511d3b1866f0636”}
         *   SERVER:{'sRisultato':'OK', ”aUser”:{'sNome':'Luca',sCognome:'Bertoni','sEmail':'luca.bertoni24@gmail.com','sUsername':'lucabertoni','sPassword':'b9be11166d72e9e3ae7fd407165e4bd2','nLivello':1}} | {'sRisultato':'NO'}
         * */
        Map<String,String> aUser = oClient.getAllUserInfo("28c8edde3d61a041121511d3b1866f0636");
        oText.setText(aUser.get("sNome") + "\n" + aUser.get("sCognome") + "\n" + aUser.get("sEmail") + "\n" + aUser.get("sUsername") + "\n" + aUser.get("sPassword") + "\n" + aUser.get("nLivello"));
    }
}