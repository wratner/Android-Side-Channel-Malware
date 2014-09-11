package com.example.cs463mp2;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;

import android.annotation.SuppressLint;
import android.app.Service;
import android.content.Intent;
import android.net.TrafficStats;
import android.os.Binder;
import android.os.Handler;
import android.os.IBinder;
import android.os.Message;
import android.util.Log;
import android.widget.Toast;

public class MonitorService extends Service {
	
	private final IBinder mBinder = new MyBinder();
	private long StartRxBytes = 0;
	private long tempRxBytes = 0;
	private long StartTxBytes = 0;
	private long tempTxBytes = 0;
	private long StartRxPackets = 0;
	private long tempRxPackets = 0;
	private long StartTxPackets = 0;
	private long tempTxPackets = 0;
	Handler handler;
	public int stop = 0;
	public int UID = 10070;
	public Runnable mRun;

	@SuppressLint("HandlerLeak")
	public void onStart(Intent intent, int startId) {
		Toast.makeText(this, "Service running", Toast.LENGTH_SHORT).show();
		handler = new Handler() {

			@Override
			public void handleMessage(Message msg) {
				super.handleMessage(msg);
				StartRxBytes = TrafficStats.getUidRxBytes(UID);
				StartTxBytes = TrafficStats.getUidTxBytes(UID);
				StartRxPackets = TrafficStats.getUidRxPackets(UID);
				StartTxPackets = TrafficStats.getUidTxPackets(UID);
				if (StartRxBytes != tempRxBytes || StartTxBytes != tempTxBytes
						|| StartRxPackets != tempRxPackets
						|| StartTxPackets != tempTxPackets) {
					Log.i("Difference detected", "Difference in files detected");
					/*File root = android.os.Environment
							.getExternalStorageDirectory();
					File dir = new File(root.getAbsolutePath()
							+ "/webMDTraffic");
					dir.mkdirs();*/
				/*	ContextWrapper cw = new ContextWrapper(getBaseContext());
					File dir = cw.getDir("root", Context.MODE_PRIVATE);*/
					File dir = getFilesDir();
					File file = new File(dir, "test.txt");
					try {
						BufferedWriter writer = new BufferedWriter(
								new FileWriter(file, true));
						writer.write(String.valueOf(System.currentTimeMillis() / 1000L)
								+ "; "
								+ String.valueOf(StartRxBytes)
								+ "; "
								+ String.valueOf(StartTxBytes)
								+ "; "
								+ String.valueOf(StartRxPackets)
								+ "; "
								+ String.valueOf(StartTxPackets));
						writer.newLine();
						writer.flush();
						writer.close();
					} catch (FileNotFoundException e) {
						e.printStackTrace();
						Log.e("Error", "File Not found", e);
					} catch (IOException e) {
						e.printStackTrace();
						Log.e("Error", "IO ERROR", e);
					}
				}
				if (StartRxBytes != tempRxBytes) {
					Log.i("Monitor Traffic", "Starting to monitor traffic now");
					tempRxBytes = StartRxBytes;
					Log.i("RxBytes Change",
							"StartRxBytes is: " + String.valueOf(StartRxBytes));
				}
				if (StartTxBytes != tempTxBytes) {
					tempTxBytes = StartTxBytes;
					Log.i("TxBytes Change",
							"StartTxBytes is : " + String.valueOf(StartTxBytes));
				}
				if (StartRxPackets != tempRxPackets) {
					//Log.i("Monitor Traffic", "Starting to monitor traffic now");
					tempRxPackets = StartRxPackets;
					Log.i("RxPackets Change",
							"StartRxPackets is: " + String.valueOf(StartRxPackets));
				}
				if (StartTxPackets != tempTxPackets) {
					//Log.i("Monitor Traffic", "Starting to monitor traffic now");
					tempTxPackets = StartTxPackets;
					Log.i("TxPackets Change",
							"StartTxPackets is: " + String.valueOf(StartTxPackets));
				}
			}

		};

		new Thread(mRun = new Runnable() {
			public void run() {
				while (stop == 0) {
					try {
						Thread.sleep(100);
						handler.sendEmptyMessage(0);

					} catch (InterruptedException e) {
						e.printStackTrace();
					}

				}

			}
		}).start();
	}



	public void setStop() {
		stop = 1;
	}
	public void setStopOff() {
		stop = 0;
	}
	public int getStop() {
		return stop;
	}

	public IBinder onBind(Intent arg0) {
		return mBinder;
	}

	public class MyBinder extends Binder {
		MonitorService getService() {
			return MonitorService.this;
		}
	}
}
