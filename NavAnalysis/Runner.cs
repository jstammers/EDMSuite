﻿using System;
using System.Collections.Generic;
using System.Windows.Forms;
using System.Runtime.Remoting;
using System.Runtime.Remoting.Channels;
using System.Runtime.Remoting.Channels.Tcp;

namespace NavAnalysis
{
    static class Runner
    {
        [STAThread]
        static void Main()
        {
            // instantiate the controller
            Controller controller = new Controller();

            // publish the controller to the remoting system
            TcpChannel channel = new TcpChannel(1188);
            ChannelServices.RegisterChannel(channel, false);
            RemotingServices.Marshal(controller, "controller.rem");

            // hand over to the controller
            controller.Start();

            // the application is finishing - close down the remoting channel
            RemotingServices.Disconnect(controller);
            ChannelServices.UnregisterChannel(channel);
        }
    }
}
