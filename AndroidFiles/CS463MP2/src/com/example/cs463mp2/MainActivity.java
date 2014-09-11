package com.example.cs463mp2;


import java.io.File;
import java.text.SimpleDateFormat;
import java.util.List;

import android.app.Activity;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;
import android.view.View;
import android.widget.Button;

public class MainActivity extends Activity {
	private MonitorService s;
	private int UID;
	public SimpleDateFormat dateFormat = new SimpleDateFormat(
			"yyyy-MM-dd HH:mm:ss");
	public String currentTimeStamp = null;
	
	public int i = 0;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		final Button stopButton = (Button) findViewById(R.id.stopButton);
		final PackageManager pm = getPackageManager();
		List<ApplicationInfo> packages = pm
				.getInstalledApplications(PackageManager.GET_META_DATA);
		for (ApplicationInfo packageInfo : packages) {
			if (packageInfo.packageName.equals("com.webmd.android")) {
				this.UID = packageInfo.uid;
			}
			Log.i("Check UID", "UID is: " + UID);

		}

		stopButton.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				s.setStop();
			}
		});
	}
	public void startMonitoring(View view) {
		if(s.getStop() != 0)
			s.setStopOff();
		/*File root = android.os.Environment
				.getExternalStorageDirectory();*/
		/*File dir = new File(root.getAbsolutePath()
				+ "/webMDTraffic");*/
		//ContextWrapper cw = new ContextWrapper(getBaseContext());
		//File dir = cw.getDir("root", Context.MODE_PRIVATE);
		File dir = getFilesDir();
		File file = new File(dir, "test.txt");
		if(file.exists()) 
			file.delete();
		//if(dir.exists())
			//dir.delete();
		Intent i = new Intent(getBaseContext(), MonitorService.class);
		getBaseContext().startService(i);
	}
	protected void onResume() {
		super.onResume();
		Intent intent = new Intent(this, MonitorService.class);
		bindService(intent, mConnection, Context.BIND_AUTO_CREATE);
	}

	protected void onPause() {
		super.onPause();
		unbindService(mConnection);
	}

	private ServiceConnection mConnection = new ServiceConnection() {
		public void onServiceConnected(ComponentName className, IBinder binder) {
			MonitorService.MyBinder b = (MonitorService.MyBinder) binder;
			s = b.getService();
			/*Toast.makeText(MainActivity.this, "Connected", Toast.LENGTH_SHORT)
					.show();*/
			
		}

		public void onServiceDisconnected(ComponentName className) {
			s = null;
		}
	};

}
