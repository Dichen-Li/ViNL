# SPDX-FileCopyrightText: Copyright (c) 2021 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Copyright (c) 2021 ETH Zurich, Nikita Rudin

from base64 import encode
from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

"""
changes from a1 to aliengo
- pd gains
- starting height
- target height?
- action scale
"""


class SpiderpiLbcCfg(LeggedRobotCfg):
    class env(LeggedRobotCfg.env):
        # num_envs = 30
        num_envs = 1#ldc
        # num_envs = 4096 # was getting a seg fault
        # num_envs = 2
        # num_actions = 12
        num_actions = 18#ldc
        # num_observations = 235
        num_observations = 253#ldc
        # num_proprio_obs = 48
        num_proprio_obs = 66#ldc
        save_im = True
        # camera_res = [1280, 720]
        # camera_res = [640, 360]
        camera_res = [320, 180]
        camera_type = "d"  # rgb
        num_privileged_obs = None  # 187
        train_type = "lbc"  # standard, priv, lbc

        follow_cam=False
        float_cam=False

    class terrain(LeggedRobotCfg.terrain):
        terrain_proportions = [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
        mesh_type = "trimesh"

    class init_state(LeggedRobotCfg.init_state):
        pos = [0.0, 0.0, 0.38]  # x,y,z [m]

        # default_joint_angles = {  # = target angles [rad] when action = 0.0
        #     "FL_hip_joint": 0.1,  # [rad]
        #     "RL_hip_joint": 0.1,  # [rad]
        #     "FR_hip_joint": -0.1,  # [rad]
        #     "RR_hip_joint": -0.1,  # [rad]
        #     "FL_thigh_joint": 0.8,  # [rad]
        #     "RL_thigh_joint": 1.0,  # [rad]
        #     "FR_thigh_joint": 0.8,  # [rad]
        #     "RR_thigh_joint": 1.0,  # [rad]
        #     "FL_calf_joint": -1.5,  # [rad]
        #     "RL_calf_joint": -1.5,  # [rad]
        #     "FR_calf_joint": -1.5,  # [rad]
        #     "RR_calf_joint": -1.5,  # [rad]
        # }
        default_joint_angles = {  # = target angles [rad] when action = 0.0
            "body_leg_0": 0,  # [rad]
            "leg_0_1_2": 1,  # [rad]
            "leg_0_2_3": 1,  # [rad]
            "body_leg_1": 0,  # [rad]
            "leg_1_1_2": 1,  # [rad]
            "leg_1_2_3": 1,  # [rad]
            "body_leg_2": 0,  # [rad]
            "leg_2_1_2": 1,  # [rad]
            "leg_2_2_3": 1,  # [rad]
            "body_leg_3": 0,  # [rad]
            "leg_3_1_2": 1,  # [rad]
            "leg_3_2_3": 1,  # [rad]
            "body_leg_4": 0,  # [rad]
            "leg_4_1_2": 1,  # [rad]
            "leg_4_2_3": 1,  # [rad]
            "body_leg_5": 0,  # [rad]
            "leg_5_1_2": 1,  # [rad]
            "leg_5_2_3": 1,  # [rad]
        }

    class control(LeggedRobotCfg.control):
        # PD Drive parameters:
        control_type = "P"
        # stiffness = {'joint': 20.}  # [N*m/rad]
        stiffness = {"joint": 40.0}  # [N*m/rad]
        # damping = {'joint': 0.5}     # [N*m*s/rad]
        damping = {"joint": 2.0}  # [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.25
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4

    class asset(LeggedRobotCfg.asset):
        # file = "{LEGGED_GYM_ROOT_DIR}/resources/robots/aliengo/urdf/aliengo.urdf"
        file = "{LEGGED_GYM_ROOT_DIR}/resources/robots/spiderpi/urdf/spiderpi.urdf"#ldc#urdf
        # foot_name = "foot"
        foot_name=['dummy_eef_0', 'dummy_eef_1', 'dummy_eef_2', 'dummy_eef_3', 'dummy_eef_4', 'dummy_eef_5']#ldc#name the feet to be referenced in legged_robot.py
        # penalize_contacts_on = ["thigh", "calf"]
        penalize_contacts_on=[#ldc
            'leg_0_2',
            'leg_0_3',
            'leg_1_2',
            'leg_1_3',
            'leg_2_2',
            'leg_2_3',
            'leg_3_2',
            'leg_3_3',
            'leg_4_2',
            'leg_4_3',
            'leg_5_2',
            'leg_5_3']
        # terminate_after_contacts_on = ["base", "trunk", "hip"]
        terminate_after_contacts_on=[]#ldc
        self_collisions = 1  # 1 to disable, 0 to enable...bitwise filter

    class domain_rand(LeggedRobotCfg.domain_rand):
        randomize_base_mass = True
        added_mass_range = [-5.0, 5.0]

    class rewards(LeggedRobotCfg.rewards):
        base_height_target = 0.5
        max_contact_force = 500.0
        only_positive_rewards = True

        class scales(LeggedRobotCfg.rewards.scales):
            feet_step = -1.0
            # feet_step = 0.0
            feet_stumble = -1.0
            # feet_stumble = 0.0

    class evals(LeggedRobotCfg.evals):
        feet_stumble = True
        feet_step = True
        crash_freq = True
        any_contacts = True

    class commands(LeggedRobotCfg.commands):
        class ranges:
            lin_vel_x = [0.0, 1.0]  # min max [m/s]
            lin_vel_y = [0.0, 0.0]  # min max [m/s]
            ang_vel_yaw = [-0.3, 0.3]  # min max [rad/s]
            heading = [0.0, 1.14]

    class noise(LeggedRobotCfg.noise):
        add_noise = False


class SpiderpiLbcCfgPPO(LeggedRobotCfgPPO):
    class obsSize(LeggedRobotCfgPPO.obsSize):
        encoder_hidden_dims = [128, 64, 32]
        cnn_out_size = 32
        num_dm_encoder_obs = 187

    class runner(LeggedRobotCfgPPO.runner):
        alg = "lbc"
        run_name = "debug"
        # run_name = ""
        experiment_name = "lbc_spiderpi"
        load_run = -1
        max_iterations = 10000  # number of policy updates
        num_test_envs = 1

        # resume = True #True for eval, false for train#ldc#look at this. Set it to False when training.
        resume = False #True for eval, false for train#ldc#look at this. Set it to False when training.

        resume_path = "weights/5.10spiderpi/lbc.pt"

        teacher_policy = "weights/5.10spiderpi/obs.pt"

    class lbc(LeggedRobotCfgPPO.lbc):
        batch_size = 10